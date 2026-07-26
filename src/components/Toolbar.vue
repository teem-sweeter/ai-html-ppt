<template>
  <div class="toolbar">
    <div class="toolbar-group">
      <button class="toolbar-btn" @click="$emit('fullscreen')" title="全屏">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M8 3H5a2 2 0 00-2 2v3m18 0V5a2 2 0 00-2-2h-3m0 18h3a2 2 0 002-2v-3M3 16v3a2 2 0 002 2h3"/>
        </svg>
        <span>全屏</span>
      </button>
    </div>
    
    <div class="toolbar-divider"></div>
    
    <div class="toolbar-group">
      <button class="toolbar-btn" @click="$emit('download-png')" title="下载 PNG">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
          <circle cx="8.5" cy="8.5" r="1.5"/>
          <polyline points="21 15 16 10 5 21"/>
        </svg>
        <span>PNG</span>
      </button>
      
      <button class="toolbar-btn" @click="$emit('download-svg')" title="下载 SVG">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/>
          <polyline points="14 2 14 8 20 8"/>
          <line x1="16" y1="13" x2="8" y2="13"/>
          <line x1="16" y1="17" x2="8" y2="17"/>
        </svg>
        <span>SVG</span>
      </button>
      
      <button class="toolbar-btn" @click="$emit('export-html')" title="导出 HTML">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="16 18 22 12 16 6"/>
          <polyline points="8 6 2 12 8 18"/>
        </svg>
        <span>HTML</span>
      </button>
    </div>
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
  gap: 8px;
  padding: 8px 16px;
  background: var(--surface);
  border-radius: var(--radius);
  border: 1px solid var(--border);
}

.toolbar-group {
  display: flex;
  align-items: center;
  gap: 4px;
}

.toolbar-divider {
  width: 1px;
  height: 24px;
  background: var(--divider);
  margin: 0 8px;
}

.toolbar-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  border: none;
  background: transparent;
  color: var(--text-secondary);
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  transition: all 0.2s ease;
}

.toolbar-btn:hover {
  background: var(--surface-2);
  color: var(--text-primary);
}

.toolbar-btn:active {
  background: var(--surface-3);
  transform: scale(0.98);
}

.toolbar-btn svg {
  flex-shrink: 0;
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