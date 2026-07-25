<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import Sidebar from './components/Sidebar.vue'
import Player from './components/Player.vue'
import ProgressBar from './components/ProgressBar.vue'
import { PRESENTATIONS, workspacesReady } from './presentations/registry'

const currentPptId = ref('pooling')
const currentPage = ref(0)
const ready = ref(false)

const currentPresentation = computed(() => {
  return PRESENTATIONS.find(p => p.id === currentPptId.value) || PRESENTATIONS[0]
})

// 从URL查询参数初始化状态
onMounted(async () => {
  // 等待工作空间加载完成
  await workspacesReady
  ready.value = true

  const params = new URLSearchParams(window.location.search)
  const pptId = params.get('ppt')
  const page = params.get('page')
  
  if (pptId && PRESENTATIONS.find(p => p.id === pptId)) {
    currentPptId.value = pptId
  }
  if (page && !isNaN(Number(page))) {
    currentPage.value = Number(page)
  }
})

// 更新URL查询参数
function updateUrl() {
  const params = new URLSearchParams()
  params.set('ppt', currentPptId.value)
  params.set('page', currentPage.value.toString())
  window.history.replaceState({}, '', `${window.location.pathname}?${params.toString()}`)
}

// 监听状态变化更新URL
watch([currentPptId, currentPage], updateUrl)

// 当切换PPT时重置页码
watch(currentPptId, () => {
  currentPage.value = 0
})
</script>

<template>
  <div class="app" v-if="ready">
    <Sidebar 
      :current-ppt-id="currentPptId"
      @update:current-ppt-id="currentPptId = $event"
    />
    <div class="main-content">
      <Player 
        v-if="currentPresentation"
        :presentation="currentPresentation"
        :current-page="currentPage"
        @update:current-page="currentPage = $event"
      />
      <ProgressBar 
        v-if="currentPresentation"
        :total="currentPresentation.totalSlides"
        :current="currentPage"
        @update:current-page="currentPage = $event"
      />
    </div>
  </div>
  <div v-else class="loading">
    <p>加载中...</p>
  </div>
</template>

<style scoped>
.app {
  display: flex;
  height: 100vh;
  width: 100vw;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.loading {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: var(--text-muted);
}
</style>