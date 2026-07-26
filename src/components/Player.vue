<template>
  <div class="player">
    <div class="slide-container" ref="slideContainer">
      <iframe
        ref="iframeRef"
        class="slide-iframe"
        frameborder="0"
        :src="iframeUrl"
        :style="{ visibility: iframeReady ? 'visible' : 'hidden' }"
        @load="onIframeLoad"
      ></iframe>
      <div class="click-overlay" @click="handleClick"></div>
      <div v-if="!iframeReady" class="loading-overlay">
        <div class="loading-spinner"></div>
        <div class="loading-text">加载中...</div>
      </div>
      <div class="slide-counter">
        {{ currentPage + 1 }} / {{ presentation.totalSlides }}
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
import { toPng, toSvg } from 'html-to-image'
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
  isDark?: boolean
}>()

const emit = defineEmits<{
  'update:currentPage': [page: number]
}>()

const isFullscreen = ref(false)
const slideContainer = ref<HTMLDivElement | null>(null)
const iframeRef = ref<HTMLIFrameElement | null>(null)
const iframeReady = ref(false)
const touchStartX = ref(0)

const iframeUrl = ref('')

function getIframeUrl() {
  return `/workspaces/${props.presentation.workspace}/${props.presentation.id}/${props.presentation.file}`
}

function onIframeLoad() {
  // 延迟执行，确保iframe中的JavaScript已经加载完成
  setTimeout(() => {
    injectControlScript()
    // 直接切换到当前页
    navigateToSlide(props.currentPage)
    iframeReady.value = true
  }, 500)
}

function navigateToSlide(index: number) {
  if (!iframeRef.value?.contentDocument) return
  
  const slides = iframeRef.value.contentDocument.querySelectorAll('.slide')
  if (!slides || slides.length === 0) return
  
  // 移除所有active类
  slides.forEach((s: Element) => s.classList.remove('active'))
  
  // 添加active类到目标slide
  if (slides[index]) {
    slides[index].classList.add('active')
  }
}

function injectControlScript() {
  if (!iframeRef.value?.contentDocument) return
  try {
    const script = iframeRef.value.contentDocument.createElement('script')
    script.textContent = `
      // 隐藏导航栏
      var navBar = document.querySelector('.nav-bar');
      if (navBar) navBar.style.display = 'none';
      
      // 确保presentation填满视口
      var pres = document.querySelector('.presentation');
      if (pres) { 
        pres.style.width = '100vw'; 
        pres.style.height = '100vh'; 
      }
      
      // 监听消息
      window.addEventListener('message', function(e) {
        if (e.data && e.data.type === 'goToSlide') {
          // 确保goTo函数存在
          if (typeof goTo === 'function') {
            goTo(e.data.index);
          } else {
            // 备用方案：直接操作DOM
            var slides = document.querySelectorAll('.slide');
            if (slides[e.data.index]) {
              // 移除所有active类
              slides.forEach(function(s) { s.classList.remove('active'); });
              // 添加active类到目标slide
              slides[e.data.index].classList.add('active');
            }
          }
        }
      });
      
      console.log('Control script injected successfully');
    `
    iframeRef.value.contentDocument.head.appendChild(script)
  } catch (e) {
    console.error('inject script error:', e)
  }
}

watch(() => props.isDark, (newVal) => {
  if (iframeRef.value?.contentWindow) {
    iframeRef.value.contentWindow.postMessage({ type: 'themeChange', isDark: newVal }, '*')
  }
})

// 监听PPT切换
watch(() => [props.presentation.workspace, props.presentation.id], () => {
  iframeReady.value = false
  iframeUrl.value = getIframeUrl()
})

// 监听页码变化
watch(() => props.currentPage, (newPage) => {
  navigateToSlide(newPage)
})

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

async function downloadPng() {
  if (!iframeRef.value?.contentDocument?.body) {
    alert('无法访问页面内容')
    return
  }
  try {
    const node = iframeRef.value.contentDocument.body
    const dataUrl = await toPng(node, {
      width: iframeRef.value.contentWindow?.innerWidth || 1920,
      height: iframeRef.value.contentWindow?.innerHeight || 1080,
      pixelRatio: 2,
      backgroundColor: '#0a0a0f'
    })
    const a = document.createElement('a')
    a.href = dataUrl
    a.download = `${props.presentation.id}-slide${props.currentPage + 1}.png`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
  } catch (e) {
    console.error('Download PNG error:', e)
    alert('下载PNG失败')
  }
}

async function downloadSvg() {
  if (!iframeRef.value?.contentDocument?.body) {
    alert('无法访问页面内容')
    return
  }
  try {
    const node = iframeRef.value.contentDocument.body
    const dataUrl = await toSvg(node, {
      width: iframeRef.value.contentWindow?.innerWidth || 1920,
      height: iframeRef.value.contentWindow?.innerHeight || 1080,
      backgroundColor: '#0a0a0f'
    })
    const a = document.createElement('a')
    a.href = dataUrl
    a.download = `${props.presentation.id}-slide${props.currentPage + 1}.svg`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
  } catch (e) {
    console.error('Download SVG error:', e)
    alert('下载SVG失败')
  }
}

function exportHtml() {
  if (!iframeRef.value?.contentDocument) {
    alert('无法访问页面内容')
    return
  }
  try {
    const doc = iframeRef.value.contentDocument
    const html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${props.presentation.title} - Slide ${props.currentPage + 1}</title>
</head>
<body>
${doc.body.innerHTML}
</body>
</html>`
    const blob = new Blob([html], { type: 'text/html;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${props.presentation.id}-slide${props.currentPage + 1}.html`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
  } catch (e) {
    console.error('Export HTML error:', e)
    alert('导出HTML失败')
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
  document.addEventListener('fullscreenchange', handleFullscreenChange)
  slideContainer.value?.addEventListener('touchstart', handleTouchStart)
  slideContainer.value?.addEventListener('touchend', handleTouchEnd)
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
  align-items: center;
  justify-content: center;
  background: var(--bg);
  padding: 24px;
}

.slide-container {
  width: 100%;
  max-width: 1280px;
  aspect-ratio: 16 / 9;
  background: var(--surface);
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.slide-iframe {
  width: 100%;
  height: 100%;
  border: none;
  display: block;
}

.click-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  cursor: pointer;
}

.slide-counter {
  position: absolute;
  bottom: 16px;
  right: 16px;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
  opacity: 0;
  transition: opacity 0.2s ease;
}

.slide-container:hover .slide-counter {
  opacity: 1;
}

.loading-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: var(--surface);
  z-index: 5;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid var(--surface-3);
  border-top-color: var(--primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin-bottom: 16px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-text {
  font-size: 14px;
  color: var(--text-secondary);
}

.slide-container:fullscreen {
  width: 100vw;
  height: 100vh;
  max-width: none;
  aspect-ratio: auto;
  border-radius: 0;
  box-shadow: none;
}

.slide-container:fullscreen .slide-counter {
  opacity: 1;
}

@media (max-width: 768px) {
  .player {
    padding: 12px;
  }
  
  .slide-container {
    border-radius: var(--radius-lg);
  }
}
</style>