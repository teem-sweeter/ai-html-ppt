<template>
  <div class="toolbar">
    <button class="toolbar-btn" @click="$emit('fullscreen')" title="全屏">
      <span class="btn-icon">⛶</span>
    </button>
    <button class="toolbar-btn" @click="$emit('download-png')" title="下载PNG">
      <span class="btn-icon">📷</span>
    </button>
    <button class="toolbar-btn" @click="$emit('download-svg')" title="下载SVG">
      <span class="btn-icon">🎨</span>
    </button>
    <button class="toolbar-btn" @click="$emit('export-html')" title="导出HTML">
      <span class="btn-icon">📄</span>
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
  position: fixed;
  right: 16px;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  gap: 8px;
  z-index: 100;
}

.toolbar-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text-primary);
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 18px;
}

.toolbar-btn:hover {
  background: var(--accent);
  border-color: var(--accent);
  color: var(--bg);
}
</style>