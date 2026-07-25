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
      <button class="fullscreen-btn" @click.stop="toggleFullscreen" :title="isFullscreen ? '退出全屏' : '全屏'">
        {{ isFullscreen ? '⊡' : '⛶' }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'

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
  align-items: center;
  justify-content: center;
  background: #000;
  padding: 1rem;
}

.slide-container {
  width: 100%;
  max-width: 1280px;
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

.fullscreen-btn {
  position: absolute;
  top: 10px; right: 10px;
  z-index: 20;
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
  width: 36px; height: 36px;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  opacity: 0;
  transition: opacity 0.2s ease;
}

.slide-container:hover .fullscreen-btn { opacity: 1; }
.fullscreen-btn:hover { background: rgba(0, 0, 0, 0.8); border-color: var(--accent); }

.slide-container:fullscreen {
  width: 100vw; height: 100vh;
  max-width: none; aspect-ratio: auto;
  border-radius: 0; box-shadow: none;
}

.slide-container:fullscreen .fullscreen-btn {
  opacity: 1; top: 20px; right: 20px;
  width: 44px; height: 44px; font-size: 22px;
}

@media (max-width: 768px) {
  .player { padding: 0.5rem; }
  .slide-container { border-radius: 2px; }
  .fullscreen-btn { opacity: 1; width: 32px; height: 32px; font-size: 16px; }
}
</style>