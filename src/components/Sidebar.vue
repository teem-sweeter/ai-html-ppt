<template>
  <div class="sidebar">
    <div class="sidebar-header">
      <h2>PPT列表</h2>
    </div>
    <div class="ppt-list">
      <div 
        v-for="ppt in presentations" 
        :key="ppt.id"
        :class="['ppt-item', { active: ppt.id === currentPptId }]"
        @click="$emit('update:currentPptId', ppt.id)"
      >
        <div class="ppt-title">{{ ppt.title }}</div>
        <div class="ppt-description">{{ ppt.description }}</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { PRESENTATIONS } from '@/presentations/registry'

defineProps<{
  currentPptId: string
}>()

defineEmits<{
  'update:currentPptId': [id: string]
}>()

const presentations = PRESENTATIONS
</script>

<style scoped>
.sidebar {
  width: 280px;
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
}

.sidebar-header h2 {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
}

.ppt-list {
  flex: 1;
  overflow-y: auto;
  padding: 0.5rem;
}

.ppt-item {
  padding: 1rem;
  margin: 0.5rem 0;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.ppt-item:hover {
  background: var(--surface-2);
}

.ppt-item.active {
  background: var(--accent);
  color: var(--bg);
}

.ppt-item.active .ppt-title {
  color: var(--bg);
}

.ppt-item.active .ppt-description {
  color: rgba(0, 0, 0, 0.7);
}

.ppt-title {
  font-weight: 600;
  margin-bottom: 0.25rem;
  color: var(--text-primary);
}

.ppt-description {
  font-size: 0.875rem;
  color: var(--text-muted);
}

/* 滚动条美化 */
.ppt-list::-webkit-scrollbar {
  width: 6px;
}

.ppt-list::-webkit-scrollbar-track {
  background: transparent;
}

.ppt-list::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 3px;
}

.ppt-list::-webkit-scrollbar-thumb:hover {
  background: var(--text-muted);
}
</style>