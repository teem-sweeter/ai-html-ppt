<template>
  <div class="progress-bar">
    <div class="nav-progress">
      <div 
        v-for="page in total" 
        :key="page" 
        :class="['nav-dot', { active: page - 1 === current }]"
        @click="$emit('update:currentPage', page - 1)"
      ></div>
    </div>
    <div class="nav-controls">
      <button 
        class="nav-btn" 
        :disabled="current === 0"
        @click="$emit('update:currentPage', current - 1)"
      >
        ← Prev
      </button>
      <span class="nav-page">{{ current + 1 }} / {{ total }}</span>
      <button 
        class="nav-btn" 
        :disabled="current === total - 1"
        @click="$emit('update:currentPage', current + 1)"
      >
        Next →
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  total: number
  current: number
}>()

defineEmits<{
  'update:currentPage': [page: number]
}>()
</script>

<style scoped>
.progress-bar {
  padding: 1rem 2rem;
  background: var(--surface);
  border-top: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.nav-progress {
  display: flex;
  gap: 6px;
  align-items: center;
  justify-content: center;
}

.nav-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--grid-border);
  transition: all 0.3s ease;
  cursor: pointer;
}

.nav-dot.active {
  background: var(--accent);
  box-shadow: 0 0 10px rgba(0, 229, 255, 0.4);
  width: 24px;
  border-radius: 4px;
}

.nav-controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-btn {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  color: var(--text-muted);
  padding: 6px 16px;
  border-radius: 3px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.nav-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.nav-btn:disabled {
  opacity: 0.2;
  cursor: default;
}

.nav-btn:disabled:hover {
  border-color: var(--grid-border);
  color: var(--text-muted);
}

.nav-page {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: var(--text-muted);
}
</style>