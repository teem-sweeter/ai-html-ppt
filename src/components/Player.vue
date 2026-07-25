<template>
  <div class="player">
    <div class="slide-container" ref="slideContainer" @click="handleClick">
      <component :is="currentSlideComponent" class="slide active" />
      <button class="fullscreen-btn" @click.stop="toggleFullscreen" :title="isFullscreen ? '退出全屏' : '全屏'">
        {{ isFullscreen ? '⊡' : '⛶' }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, onMounted, onUnmounted, defineAsyncComponent } from 'vue'

interface Presentation {
  id: string
  title: string
  description: string
  slides: Array<() => Promise<any>>
}

const props = defineProps<{
  presentation: Presentation
  currentPage: number
}>()

const emit = defineEmits<{
  'update:currentPage': [page: number]
}>()

const loading = ref(false)
const isFullscreen = ref(false)
const slideContainer = ref<HTMLDivElement | null>(null)
const touchStartX = ref(0)

const currentSlideComponent = computed(() => {
  if (!props.presentation.slides[props.currentPage]) {
    return null
  }
  return defineAsyncComponent(() => {
    loading.value = true
    return props.presentation.slides[props.currentPage]().finally(() => {
      loading.value = false
    })
  })
})

function handleKeydown(event: KeyboardEvent) {
  if (event.key === 'ArrowRight' || event.key === 'ArrowDown' || event.key === ' ') {
    event.preventDefault()
    if (props.currentPage < props.presentation.slides.length - 1) {
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
    slideContainer.value.requestFullscreen().then(() => {
      isFullscreen.value = true
    }).catch(err => {
      console.log('全屏请求失败:', err)
    })
  } else {
    document.exitFullscreen().then(() => {
      isFullscreen.value = false
    }).catch(err => {
      console.log('退出全屏失败:', err)
    })
  }
}

function handleFullscreenChange() {
  // 检查当前全屏元素是否是slideContainer
  isFullscreen.value = document.fullscreenElement === slideContainer.value
}

function handleClick(event: MouseEvent) {
  const container = event.currentTarget as HTMLElement
  const rect = container.getBoundingClientRect()
  const clickX = event.clientX - rect.left
  const containerWidth = rect.width
  
  // 点击左侧1/3区域上一页，右侧2/3区域下一页
  if (clickX < containerWidth / 3) {
    // 上一页
    if (props.currentPage > 0) {
      emit('update:currentPage', props.currentPage - 1)
    }
  } else {
    // 下一页
    if (props.currentPage < props.presentation.slides.length - 1) {
      emit('update:currentPage', props.currentPage + 1)
    }
  }
}

function handleTouchStart(event: TouchEvent) {
  touchStartX.value = event.changedTouches[0].screenX
}

function handleTouchEnd(event: TouchEvent) {
  const touchEndX = event.changedTouches[0].screenX
  const diff = touchStartX.value - touchEndX
  
  // 滑动距离超过60px时触发翻页
  if (Math.abs(diff) > 60) {
    if (diff > 0) {
      // 向左滑动，下一页
      if (props.currentPage < props.presentation.slides.length - 1) {
        emit('update:currentPage', props.currentPage + 1)
      }
    } else {
      // 向右滑动，上一页
      if (props.currentPage > 0) {
        emit('update:currentPage', props.currentPage - 1)
      }
    }
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
  document.addEventListener('fullscreenchange', handleFullscreenChange)
  
  // 添加触摸事件监听器
  if (slideContainer.value) {
    slideContainer.value.addEventListener('touchstart', handleTouchStart)
    slideContainer.value.addEventListener('touchend', handleTouchEnd)
  }
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
  document.removeEventListener('fullscreenchange', handleFullscreenChange)
  
  // 移除触摸事件监听器
  if (slideContainer.value) {
    slideContainer.value.removeEventListener('touchstart', handleTouchStart)
    slideContainer.value.removeEventListener('touchend', handleTouchEnd)
  }
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

/* 点击区域提示 */
.slide-container::before,
.slide-container::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  z-index: 10;
  opacity: 0;
  transition: opacity 0.2s ease;
}

.slide-container:hover::before,
.slide-container:hover::after {
  opacity: 1;
}

.slide-container::before {
  left: 0;
  width: 33%;
  background: linear-gradient(90deg, rgba(255,255,255,0.03) 0%, transparent 100%);
}

.slide-container::after {
  right: 0;
  width: 67%;
  background: linear-gradient(-90deg, rgba(255,255,255,0.03) 0%, transparent 100%);
}

/* 全屏按钮 */
.fullscreen-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 20;
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
  width: 36px;
  height: 36px;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  opacity: 0;
  transition: opacity 0.2s ease, background 0.2s ease;
}

.slide-container:hover .fullscreen-btn {
  opacity: 1;
}

.fullscreen-btn:hover {
  background: rgba(0, 0, 0, 0.8);
  border-color: var(--accent);
}

/* 全屏状态样式 */
.slide-container:fullscreen {
  width: 100vw;
  height: 100vh;
  max-width: none;
  aspect-ratio: auto;
  border-radius: 0;
  box-shadow: none;
}

.slide-container:fullscreen .fullscreen-btn {
  opacity: 1;
  top: 20px;
  right: 20px;
  width: 44px;
  height: 44px;
  font-size: 22px;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .player {
    padding: 0.5rem;
  }
  
  .slide-container {
    border-radius: 2px;
  }
  
  .fullscreen-btn {
    opacity: 1;
    width: 32px;
    height: 32px;
    font-size: 16px;
  }
}
</style>