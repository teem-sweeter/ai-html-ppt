<template>
  <div class="toolbar">
    <button class="toolbar-btn" @click="$emit('fullscreen')" title="全屏">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/>
      </svg>
      <span>全屏</span>
    </button>
    
    <div class="divider"></div>
    
    <button class="toolbar-btn" @click="$emit('download-png')" title="下载 PNG">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M19 12v7H5v-7H3v7c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-7h-2zm-6 .67l2.59-2.58L17 11.5l-5 5-5-5 1.41-1.41L11 12.67V3h2v9.67z"/>
      </svg>
      <span>PNG</span>
    </button>
    
    <button class="toolbar-btn" @click="$emit('download-svg')" title="下载 SVG">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/>
      </svg>
      <span>SVG</span>
    </button>
    
    <button class="toolbar-btn" @click="$emit('export-html')" title="导出 HTML">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/>
      </svg>
      <span>HTML</span>
    </button>
  </div>
</template>

<script setup lang="ts">
defineEmits<{
  'fullscreen': []
  'download-png': []
  'download-svg': []
  'export-html': []
}>()
</script>

<style scoped>
.toolbar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  padding: 8px 16px;
  background: var(--surface);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-1);
}

.toolbar-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border: none;
  background: transparent;
  color: var(--text-secondary);
  border-radius: var(--radius);
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.toolbar-btn:hover {
  background: var(--surface-2);
  color: var(--text-primary);
}

.toolbar-btn:active {
  background: var(--surface-3);
  transform: scale(0.98);
}

.divider {
  width: 1px;
  height: 24px;
  background: var(--divider);
  margin: 0 8px;
}

@media (max-width: 768px) {
  .toolbar {
    padding: 6px 12px;
  }
  
  .toolbar-btn span {
    display: none;
  }
  
  .toolbar-btn {
    padding: 8px;
  }
}
</style>