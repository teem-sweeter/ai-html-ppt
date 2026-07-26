<template>
  <div class="sidebar">
    <div class="sidebar-header">
      <h2>PPT 演示系统</h2>
      <button class="theme-toggle" @click="toggleTheme" :title="isDark ? '切换到白色主题' : '切换到暗色主题'">
        {{ isDark ? '☀️' : '🌙' }}
      </button>
    </div>
    <div class="workspace-list">
      <div 
        v-for="workspace in workspaces" 
        :key="workspace.id"
        class="workspace-group"
      >
        <div class="workspace-header">
          <div class="workspace-name">{{ workspace.name }}</div>
          <div class="workspace-desc">{{ workspace.description }}</div>
        </div>
        <div class="ppt-list">
          <div 
            v-for="ppt in getPresentationsByWorkspace(workspace.id)" 
            :key="ppt.id"
            :class="['ppt-item', { active: ppt.id === currentPptId }]"
            @click="$emit('update:currentPptId', ppt.id)"
          >
            <div class="ppt-title">{{ ppt.title }}</div>
            <div class="ppt-description">{{ ppt.description }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { WORKSPACES, PRESENTATIONS } from '@/presentations/registry'
import type { Presentation } from '@/presentations/registry'

defineProps<{
  currentPptId: string
}>()

defineEmits<{
  'update:currentPptId': [id: string]
}>()

const workspaces = WORKSPACES
const isDark = ref(true)

function getPresentationsByWorkspace(workspaceId: string): Presentation[] {
  return PRESENTATIONS.filter(p => p.workspace === workspaceId)
}

function toggleTheme() {
  isDark.value = !isDark.value
  applyTheme()
  localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
}

function applyTheme() {
  const root = document.documentElement
  if (isDark.value) {
    root.style.setProperty('--bg', '#0a0a0f')
    root.style.setProperty('--surface', '#12121a')
    root.style.setProperty('--surface-2', '#1a1a26')
    root.style.setProperty('--text-primary', '#eef0f6')
    root.style.setProperty('--text-muted', '#6b6d7b')
    root.style.setProperty('--border', '#2a2a3d')
  } else {
    root.style.setProperty('--bg', '#ffffff')
    root.style.setProperty('--surface', '#f5f5f7')
    root.style.setProperty('--surface-2', '#e8e8ed')
    root.style.setProperty('--text-primary', '#1d1d1f')
    root.style.setProperty('--text-muted', '#86868b')
    root.style.setProperty('--border', '#d2d2d7')
  }
}

onMounted(() => {
  const savedTheme = localStorage.getItem('theme')
  if (savedTheme) {
    isDark.value = savedTheme === 'dark'
  }
  applyTheme()
})
</script>

<style scoped>
.sidebar {
  width: 300px;
  background: var(--surface);
  border-right: 1px solid var(--border);
  height: 100vh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: 1.5rem;
  border-bottom: 1px solid var(--border);
  background: var(--surface-2);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.sidebar-header h2 {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
}

.theme-toggle {
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text-primary);
  width: 36px;
  height: 36px;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  transition: all 0.2s ease;
}

.theme-toggle:hover {
  background: var(--accent);
  border-color: var(--accent);
}

.workspace-list {
  flex: 1;
  overflow-y: auto;
  padding: 0.5rem;
}

.workspace-group {
  margin-bottom: 1rem;
}

.workspace-header {
  padding: 0.75rem 1rem;
  background: var(--surface-2);
  border-radius: 6px;
  margin-bottom: 0.5rem;
}

.workspace-name {
  font-weight: 600;
  color: var(--accent);
  font-size: 0.9rem;
}

.workspace-desc {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: 0.25rem;
}

.ppt-list {
  padding-left: 0.5rem;
}

.ppt-item {
  padding: 0.75rem 1rem;
  margin: 0.25rem 0;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  border-left: 3px solid transparent;
}

.ppt-item:hover {
  background: var(--surface-2);
  border-left-color: var(--accent);
}

.ppt-item.active {
  background: var(--accent);
  color: var(--bg);
  border-left-color: var(--accent);
}

.ppt-item.active .ppt-title {
  color: var(--bg);
  font-weight: 700;
}

.ppt-item.active .ppt-description {
  color: rgba(0, 0, 0, 0.7);
}

.ppt-title {
  font-weight: 600;
  margin-bottom: 0.25rem;
  color: var(--text-primary);
  font-size: 0.9rem;
}

.ppt-description {
  font-size: 0.75rem;
  color: var(--text-muted);
  line-height: 1.4;
}

/* 滚动条美化 */
.workspace-list::-webkit-scrollbar {
  width: 6px;
}

.workspace-list::-webkit-scrollbar-track {
  background: transparent;
}

.workspace-list::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 3px;
}

.workspace-list::-webkit-scrollbar-thumb:hover {
  background: var(--text-muted);
}
</style>