<template>
  <div class="player">
    <div class="slide-container" ref="slideContainer" @click="handleClick">
      <iframe
        ref="iframeRef"
        class="slide-iframe"
        frameborder="0"
        :src="iframeUrl"
        :style="{ visibility: iframeReady ? 'visible' : 'hidden' }"
        @load="onIframeLoad"
      ></iframe>
      <div v-if="!iframeReady" class="loading-overlay">
        <div class="loading-spinner"></div>
        <div class="loading-text">加载中...</div>
      </div>
    </div>
    <Toolbar
      @fullscreen="toggleFullscreen"
      @download-png="downloadPng"
      @download-svg="downloadSvg"
      @export-html="exportHtml"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import Toolbar from './Toolbar.vue'

interface Presentation {
  id: string
  title: string
  description: string
  workspace: string
  file: string
  totalSlides: number
}

const props = defineProps<{
  presentation: Presentation
  currentPage: number
}>()

const emit = defineEmits<{
  'update:currentPage': [page: number]
}>()

const isFullscreen = ref(false)
const slideContainer = ref<HTMLDivElement | null>(null)
const iframeRef = ref<HTMLIFrameElement | null>(null)
const iframeReady = ref(false)
const touchStartX = ref(0)
let needsNavigate = false

const iframeUrl = ref('')

function getIframeUrl() {
  return `/workspaces/${props.presentation.workspace}/${props.presentation.id}/${props.presentation.file}`
}

function goToSlide(index: number) {
  if (!iframeRef.value?.contentWindow) return
  try {
    iframeRef.value.contentWindow.postMessage({ type: 'goToSlide', index }, '*')
  } catch (e) {
    console.error('postMessage error:', e)
  }
}

function onIframeLoad() {
  injectControlScript()
  if (needsNavigate) {
    setTimeout(() => {
      goToSlide(props.currentPage)
      iframeReady.value = true
    }, 100)
    needsNavigate = false
  } else {
    iframeReady.value = true
  }
}

function injectControlScript() {
  if (!iframeRef.value?.contentDocument) return
  try {
    const script = iframeRef.value.contentDocument.createElement('script')
    script.textContent = `
      var navBar = document.querySelector('.nav-bar');
      if (navBar) navBar.style.display = 'none';
      var pres = document.querySelector('.presentation');
      if (pres) { pres.style.width = '100vw'; pres.style.height = '100vh'; }
      window.addEventListener('message', function(e) {
        if (e.data && e.data.type === 'goToSlide') {
          if (typeof goTo === 'function') { goTo(e.data.index); }
        }
      });
    `
    iframeRef.value.contentDocument.head.appendChild(script)
  } catch (e) {
    console.error('inject script error:', e)
  }
}

// 全屏
function toggleFullscreen() {
  if (!slideContainer.value) return
  if (!document.fullscreenElement) {
    slideContainer.value.requestFullscreen().then(() => { isFullscreen.value = true })
  } else {
    document.exitFullscreen().then(() => { isFullscreen.value = false })
  }
}

function handleFullscreenChange() {
  isFullscreen.value = !!document.fullscreenElement
}

// 下载PNG - 通过SVG foreignObject转Canvas
async function downloadPng() {
  if (!iframeRef.value?.contentDocument || !iframeRef.value?.contentWindow) {
    alert('无法访问页面内容')
    return
  }
  try {
    const iframeDoc = iframeRef.value.contentDocument
    const width = iframeRef.value.contentWindow.innerWidth || 1920
    const height = iframeRef.value.contentWindow.innerHeight || 1080

    // 获取iframe的样式和内容
    const css = Array.from(iframeDoc.querySelectorAll('style'))
      .map(s => s.textContent)
      .join('\n')

    // 构建带样式的HTML
    const styledHtml = `
      <html xmlns="http://www.w3.org/1999/xhtml">
        <head><style>${css}</style></head>
        <body style="margin:0;padding:0;">${iframeDoc.body.innerHTML}</body>
      </html>
    `

    // 转为SVG foreignObject
    const svg = `
      <svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}">
        <foreignObject width="100%" height="100%">
          ${styledHtml}
        </foreignObject>
      </svg>
    `

    // SVG转Blob URL
    const svgBlob = new Blob([svg], { type: 'image/svg+xml;charset=utf-8' })
    const svgUrl = URL.createObjectURL(svgBlob)

    // 创建Image加载SVG
    const img = new Image()
    img.onload = () => {
      // 绘制到Canvas
      const canvas = document.createElement('canvas')
      canvas.width = width * 2  // 2倍清晰度
      canvas.height = height * 2
      const ctx = canvas.getContext('2d')
      if (!ctx) return

      ctx.scale(2, 2)
      ctx.drawImage(img, 0, 0, width, height)
      URL.revokeObjectURL(svgUrl)

      // 导出PNG
      canvas.toBlob((blob) => {
        if (!blob) return
        const url = URL.createObjectURL(blob)
        const a = document.createElement('a')
        a.href = url
        a.download = `${props.presentation.id}-slide${props.currentPage + 1}.png`
        document.body.appendChild(a)
        a.click()
        document.body.removeChild(a)
        URL.revokeObjectURL(url)
      }, 'image/png')
    }
    img.onerror = () => {
      URL.revokeObjectURL(svgUrl)
      alert('截图失败，部分内容可能无法渲染')
    }
    img.src = svgUrl
  } catch (e) {
    console.error('Download PNG error:', e)
    alert('下载PNG失败: ' + (e as Error).message)
  }
}

// 下载SVG - 将当前页面HTML包装为SVG
function downloadSvg() {
  if (!iframeRef.value?.contentDocument) {
    alert('无法访问页面内容')
    return
  }
  try {
    const doc = iframeRef.value.contentDocument
    const html = doc.documentElement.outerHTML
    const width = iframeRef.value.contentWindow?.innerWidth || 1920
    const height = iframeRef.value.contentWindow?.innerHeight || 1080
    
    const svgContent = `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}">
  <foreignObject width="100%" height="100%">
    ${html}
  </foreignObject>
</svg>`

    downloadFile(svgContent, `${props.presentation.id}-slide${props.currentPage + 1}.svg`, 'image/svg+xml')
  } catch (e) {
    console.error('Download SVG error:', e)
    alert('下载SVG失败')
  }
}

// 导出HTML
function exportHtml() {
  if (!iframeRef.value?.contentDocument) {
    alert('无法访问页面内容')
    return
  }
  try {
    const doc = iframeRef.value.contentDocument
    const html = doc.documentElement.outerHTML
    const fullHtml = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${props.presentation.title} - Slide ${props.currentPage + 1}</title>
</head>
<body>
${html}
</body>
</html>`

    downloadFile(fullHtml, `${props.presentation.id}-slide${props.currentPage + 1}.html`, 'text/html')
  } catch (e) {
    console.error('Export HTML error:', e)
    alert('导出HTML失败')
  }
}

// 通用下载函数
function downloadFile(content: string, filename: string, mimeType: string) {
  const blob = new Blob([content], { type: mimeType })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = filename
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  URL.revokeObjectURL(url)
}

watch(() => props.currentPage, (newPage) => {
  goToSlide(newPage)
})

watch(() => [props.presentation.workspace, props.presentation.id], () => {
  needsNavigate = true
  iframeReady.value = false
  iframeUrl.value = getIframeUrl()
}, { immediate: false })

function handleKeydown(event: KeyboardEvent) {
  if (event.key === 'ArrowRight' || event.key === 'ArrowDown' || event.key === ' ') {
    event.preventDefault()
    if (props.currentPage < props.presentation.totalSlides - 1) {
      emit('update:currentPage', props.currentPage + 1)
    }
  } else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') {
    event.preventDefault()
    if (props.currentPage > 0) {
      emit('update:currentPage', props.currentPage - 1)
    }
  }
}

function handleClick(event: MouseEvent) {
  const rect = (event.currentTarget as HTMLElement).getBoundingClientRect()
  const clickX = event.clientX - rect.left
  if (clickX < rect.width / 3) {
    if (props.currentPage > 0) emit('update:currentPage', props.currentPage - 1)
  } else {
    if (props.currentPage < props.presentation.totalSlides - 1) emit('update:currentPage', props.currentPage + 1)
  }
}

function handleTouchStart(event: TouchEvent) {
  touchStartX.value = event.changedTouches[0].screenX
}

function handleTouchEnd(event: TouchEvent) {
  const diff = touchStartX.value - event.changedTouches[0].screenX
  if (Math.abs(diff) > 60) {
    if (diff > 0 && props.currentPage < props.presentation.totalSlides - 1) {
      emit('update:currentPage', props.currentPage + 1)
    } else if (diff < 0 && props.currentPage > 0) {
      emit('update:currentPage', props.currentPage - 1)
    }
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
  document.addEventListener('fullscreenchange', handleFullscreenChange)
  slideContainer.value?.addEventListener('touchstart', handleTouchStart)
  slideContainer.value?.addEventListener('touchend', handleTouchEnd)
  needsNavigate = true
  iframeReady.value = false
  iframeUrl.value = getIframeUrl()
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
  document.removeEventListener('fullscreenchange', handleFullscreenChange)
  slideContainer.value?.removeEventListener('touchstart', handleTouchStart)
  slideContainer.value?.removeEventListener('touchend', handleTouchEnd)
})
</script>

<style scoped>
.player {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: #000;
  padding: 1rem;
}

.slide-container {
  flex: 1;
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  aspect-ratio: 16 / 9;
  background: var(--bg);
  border-radius: 4px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
}

.slide-iframe {
  width: 100%;
  height: 100%;
  border: none;
  display: block;
}

.slide-container:hover::before,
.slide-container:hover::after {
  opacity: 1;
}

.slide-container::before {
  content: '';
  position: absolute;
  top: 0; bottom: 0; left: 0;
  width: 33%;
  z-index: 10;
  opacity: 0;
  transition: opacity 0.2s ease;
  background: linear-gradient(90deg, rgba(255,255,255,0.03) 0%, transparent 100%);
}

.slide-container::after {
  content: '';
  position: absolute;
  top: 0; bottom: 0; right: 0;
  width: 67%;
  z-index: 10;
  opacity: 0;
  transition: opacity 0.2s ease;
  background: linear-gradient(-90deg, rgba(255,255,255,0.03) 0%, transparent 100%);
}

.loading-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: var(--bg);
  z-index: 5;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid var(--surface-2);
  border-top-color: var(--accent);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin-bottom: 16px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-text {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  color: var(--text-muted);
}

.slide-container:fullscreen {
  width: 100vw; height: 100vh;
  max-width: none; aspect-ratio: auto;
}

@media (max-width: 768px) {
  .slide-container { aspect-ratio: auto; }
}
</style>