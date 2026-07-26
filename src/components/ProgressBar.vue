<template>
  <div class="progress-bar">
    <div class="progress-nav">
      <div class="nav-dots">
        <div 
          v-for="page in total" 
          :key="page" 
          :class="['nav-dot', { active: page - 1 === current }]"
          @click="$emit('update:currentPage', page - 1)"
        ></div>
      </div>
    </div>
    
    <div class="progress-controls">
      <button 
        class="control-btn" 
        :disabled="current === 0"
        @click="$emit('update:currentPage', current - 1)"
      >
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="15 18 9 12 15 6"/>
        </svg>
      </button>
      
      <div class="page-info">
        <span class="current-page">{{ current + 1 }}</span>
        <span class="separator">/</span>
        <span class="total-pages">{{ total }}</span>
      </div>
      
      <button 
        class="control-btn" 
        :disabled="current === total - 1"
        @click="$emit('update:currentPage', current + 1)"
      >
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="9 18 15 12 9 6"/>
        </svg>
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
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  background: var(--surface);
  border-radius: var(--radius);
  border: 1px solid var(--border);
}

.progress-nav {
  flex: 1;
}

.nav-dots {
  display: flex;
  gap: 6px;
  align-items: center;
}

.nav-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--surface-3);
  cursor: pointer;
  transition: all 0.2s ease;
}

.nav-dot:hover {
  background: var(--text-muted);
}

.nav-dot.active {
  background: var(--accent);
  width: 24px;
  border-radius: 4px;
}

.progress-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}

.control-btn {
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

.control-btn:hover:not(:disabled) {
  background: var(--surface-3);
  color: var(--text-primary);
}

.control-btn:active:not(:disabled) {
  transform: scale(0.95);
}

.control-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.page-info {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 14px;
  font-weight: 500;
  color: var(--text-primary);
  min-width: 60px;
  justify-content: center;
}

.separator {
  color: var(--text-muted);
}

@media (max-width: 768px) {
  .progress-bar {
    padding: 8px 12px;
  }
  
  .nav-dots {
    gap: 4px;
  }
  
  .nav-dot {
    width: 6px;
    height: 6px;
  }
  
  .nav-dot.active {
    width: 18px;
  }
}
</style>