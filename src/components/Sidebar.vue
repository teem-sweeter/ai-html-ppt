<template>
  <div class="sidebar">
    <div class="sidebar-header">
      <div class="header-content">
        <div class="logo">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <rect width="24" height="24" rx="6" fill="var(--accent)"/>
            <path d="M7 8h10v2H7V8zm0 3h10v2H7v-2zm0 3h7v2H7v-2z" fill="white"/>
          </svg>
          <span class="logo-text">PPT Viewer</span>
        </div>
        <button class="theme-toggle" @click="toggleTheme" :title="isDark ? '浅色模式' : '深色模式'">
          <svg v-if="isDark" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="5"/>
            <path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>
          </svg>
          <svg v-else width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/>
          </svg>
        </button>
      </div>
    </div>
    
    <div class="sidebar-content">
      <div 
        v-for="workspace in workspaces" 
        :key="workspace.id"
        class="workspace-section"
      >
        <div class="workspace-title">
          <span class="workspace-name">{{ workspace.name }}</span>
          <span class="workspace-count">{{ getPresentationsByWorkspace(workspace.id).length }}</span>
        </div>
        
        <div class="ppt-list">
          <div 
            v-for="ppt in getPresentationsByWorkspace(workspace.id)" 
            :key="ppt.id"
            :class="['ppt-item', { active: ppt.id === currentPptId }]"
            @click="$emit('update:currentPptId', ppt.id)"
          >
            <div class="ppt-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
                <line x1="8" y1="21" x2="16" y2="21"/>
                <line x1="12" y1="17" x2="12" y2="21"/>
              </svg>
            </div>
            <div class="ppt-info">
              <div class="ppt-title">{{ ppt.title }}</div>
              <div class="ppt-desc">{{ ppt.description }}</div>
            </div>
            <div class="ppt-arrow">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="9 18 15 12 9 6"/>
              </svg>
            </div>
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

const emit = defineEmits<{
  'update:currentPptId': [id: string]
  'theme-change': [isDark: boolean]
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
  emit('theme-change', isDark.value)
}

function applyTheme() {
  if (isDark.value) {
    document.documentElement.removeAttribute('data-theme')
  } else {
    document.documentElement.setAttribute('data-theme', 'light')
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
  width: 280px;
  background: var(--surface);
  border-right: 1px solid var(--border);
  height: 100vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.sidebar-header {
  padding: 16px 20px;
  border-bottom: 1px solid var(--divider);
  background: var(--surface);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-text {
  font-size: 17px;
  font-weight: 600;
  color: var(--text-primary);
  letter-spacing: -0.2px;
}

.theme-toggle {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  border: none;
  background: var(--surface-2);
  color: var(--text-secondary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.theme-toggle:hover {
  background: var(--surface-3);
  color: var(--text-primary);
}

.sidebar-content {
  flex: 1;
  overflow-y: auto;
  padding: 12px;
}

.workspace-section {
  margin-bottom: 8px;
}

.workspace-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  margin-bottom: 4px;
}

.workspace-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.workspace-count {
  font-size: 12px;
  color: var(--text-muted);
  background: var(--surface-2);
  padding: 2px 8px;
  border-radius: 10px;
}

.ppt-list {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.ppt-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all 0.2s ease;
  color: var(--text-primary);
}

.ppt-item:hover {
  background: var(--surface-2);
}

.ppt-item.active {
  background: var(--accent);
  color: white;
}

.ppt-item.active .ppt-icon {
  color: white;
}

.ppt-item.active .ppt-desc {
  color: rgba(255, 255, 255, 0.8);
}

.ppt-item.active .ppt-arrow {
  color: rgba(255, 255, 255, 0.6);
}

.ppt-icon {
  flex-shrink: 0;
  color: var(--text-muted);
}

.ppt-info {
  flex: 1;
  min-width: 0;
}

.ppt-title {
  font-size: 14px;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.ppt-desc {
  font-size: 12px;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-top: 2px;
}

.ppt-arrow {
  flex-shrink: 0;
  color: var(--text-muted);
  opacity: 0;
  transition: opacity 0.2s ease;
}

.ppt-item:hover .ppt-arrow {
  opacity: 1;
}

/* 滚动条 */
.sidebar-content::-webkit-scrollbar {
  width: 4px;
}

.sidebar-content::-webkit-scrollbar-track {
  background: transparent;
}

.sidebar-content::-webkit-scrollbar-thumb {
  background: var(--text-muted);
  border-radius: 2px;
}
</style>