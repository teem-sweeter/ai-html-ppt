<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import Sidebar from './components/Sidebar.vue'
import Player from './components/Player.vue'
import ProgressBar from './components/ProgressBar.vue'
import { PRESENTATIONS, workspacesReady } from './presentations/registry'

const currentPptId = ref('pooling')
const currentPage = ref(0)
const ready = ref(false)
const isDark = ref(true)

const currentPresentation = computed(() => {
  return PRESENTATIONS.find(p => p.id === currentPptId.value) || PRESENTATIONS[0]
})

onMounted(async () => {
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

  const savedTheme = localStorage.getItem('theme')
  if (savedTheme) {
    isDark.value = savedTheme === 'dark'
  }
})

function updateUrl() {
  const params = new URLSearchParams()
  params.set('ppt', currentPptId.value)
  params.set('page', currentPage.value.toString())
  window.history.replaceState({}, '', `${window.location.pathname}?${params.toString()}`)
}

watch([currentPptId, currentPage], updateUrl)

watch(currentPptId, () => {
  currentPage.value = 0
})

watch(isDark, (newVal) => {
  localStorage.setItem('theme', newVal ? 'dark' : 'light')
})
</script>

<template>
  <div class="app" v-if="ready">
    <Sidebar 
      :current-ppt-id="currentPptId"
      @update:current-ppt-id="currentPptId = $event"
      @theme-change="isDark = $event"
    />
    <div class="main-content">
      <Player 
        v-if="currentPresentation"
        :presentation="currentPresentation"
        :current-page="currentPage"
        :is-dark="isDark"
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
    <div class="loading-content">
      <div class="loading-spinner"></div>
      <p>加载中...</p>
    </div>
  </div>
</template>

<style scoped>
.app {
  display: flex;
  height: 100vh;
  width: 100vw;
  background: var(--bg);
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  padding-bottom: 50px;
}

.loading {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: var(--bg);
}

.loading-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid var(--surface-3);
  border-top-color: var(--primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-content p {
  color: var(--text-secondary);
  font-size: 14px;
}
</style>