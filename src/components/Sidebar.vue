<template>
  <div class="sidebar">
    <div class="sidebar-header">
      <div class="header-top">
        <div class="app-title">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="var(--primary)">
            <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14z"/>
            <path d="M7 7h10v2H7zm0 4h10v2H7zm0 4h7v2H7z"/>
          </svg>
          <span>PPT Viewer</span>
        </div>
        <button class="icon-btn" @click="toggleTheme" :title="isDark ? '浅色模式' : '深色模式'">
          <svg v-if="isDark" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1zM5.99 4.58a.996.996 0 00-1.41 0 .996.996 0 000 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41L5.99 4.58zm12.37 12.37a.996.996 0 00-1.41 0 .996.996 0 000 1.41l1.06 1.06c.39.39 1.03.39 1.41 0a.996.996 0 000-1.41l-1.06-1.06zm1.06-10.96a.996.996 0 000-1.41.996.996 0 00-1.41 0l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06zM7.05 18.36a.996.996 0 000-1.41.996.996 0 00-1.41 0l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06z"/>
          </svg>
          <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 3c-4.97 0-9 4.03-9 9s4.03 9 9 9 9-4.03 9-9c0-.46-.04-.92-.1-1.36a5.389 5.389 0 01-4.4 2.26 5.403 5.403 0 01-3.14-9.8c-.44-.06-.9-.1-1.36-.1z"/>
          </svg>
        </button>
      </div>
    </div>
    
    <div class="sidebar-content">
      <div 
        v-for="workspace in workspaces" 
        :key="workspace.id"
        class="workspace-group"
      >
        <div class="workspace-header">
          <span class="workspace-name">{{ workspace.name }}</span>
          <span class="workspace-badge">{{ getPresentationsByWorkspace(workspace.id).length }}</span>
        </div>
        
        <div class="ppt-list">
          <div 
            v-for="ppt in getPresentationsByWorkspace(workspace.id)" 
            :key="ppt.id"
            :class="['ppt-item', { active: ppt.id === currentPptId }]"
            @click="$emit('update:currentPptId', ppt.id)"
          >
            <div class="ppt-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14z"/>
                <path d="M7 12h10v2H7zm0-4h10v2H7zm0 8h7v2H7z"/>
              </svg>
            </div>
            <div class="ppt-info">
              <div class="ppt-title">{{ ppt.title }}</div>
              <div class="ppt-desc">{{ ppt.description }}</div>
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
  height: 100vh;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-2);
  z-index: 10;
}

.sidebar-header {
  padding: 16px;
  border-bottom: 1px solid var(--divider);
}

.header-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.app-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 18px;
  font-weight: 500;
  color: var(--text-primary);
}

.sidebar-content {
  flex: 1;
  overflow-y: auto;
  padding: 8px;
}

.workspace-group {
  margin-bottom: 8px;
}

.workspace-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  margin-bottom: 4px;
}

.workspace-name {
  font-size: 12px;
  font-weight: 500;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.workspace-badge {
  font-size: 11px;
  color: var(--text-disabled);
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
  padding: 12px;
  border-radius: var(--radius);
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  color: var(--text-primary);
}

.ppt-item:hover {
  background: var(--surface-2);
}

.ppt-item.active {
  background: var(--primary);
  color: white;
}

.ppt-item.active .ppt-icon {
  color: white;
}

.ppt-item.active .ppt-desc {
  color: rgba(255, 255, 255, 0.7);
}

.ppt-icon {
  flex-shrink: 0;
  color: var(--text-secondary);
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
  color: var(--text-secondary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-top: 2px;
}
</style>