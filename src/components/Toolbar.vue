<template>
  <div class="toolbar">
    <button class="toolbar-btn" @click="$emit('fullscreen')" title="全屏">
      <span class="btn-icon">⛶</span>
      <span class="btn-text">全屏</span>
    </button>
    <button class="toolbar-btn" @click="$emit('download-png')" title="下载PNG">
      <span class="btn-icon">📷</span>
      <span class="btn-text">PNG</span>
    </button>
    <button class="toolbar-btn" @click="$emit('download-svg')" title="下载SVG">
      <span class="btn-icon">🎨</span>
      <span class="btn-text">SVG</span>
    </button>
    <button class="toolbar-btn" @click="$emit('export-html')" title="导出HTML">
      <span class="btn-icon">📄</span>
      <span class="btn-text">HTML</span>
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
  gap: 8px;
  padding: 12px 16px;
  background: var(--surface);
  border-top: 1px solid var(--border);
}

.toolbar-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--text-primary);
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
}

.toolbar-btn:hover {
  background: var(--accent);
  border-color: var(--accent);
  color: var(--bg);
}

.btn-icon {
  font-size: 16px;
}

.btn-text {
  font-size: 12px;
}
</style>