<template>
  <div class="progress-bar">
    <div class="progress-track">
      <div class="track-fill" :style="{ width: `${(current / (total - 1)) * 100}%` }"></div>
    </div>
    
    <div class="progress-controls">
      <button 
        class="control-btn" 
        :disabled="current === 0"
        @click="$emit('update:currentPage', current - 1)"
      >
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
        </svg>
      </button>
      
      <div class="page-info">
        <span class="current">{{ current + 1 }}</span>
        <span class="separator">/</span>
        <span class="total">{{ total }}</span>
      </div>
      
      <button 
        class="control-btn" 
        :disabled="current === total - 1"
        @click="$emit('update:currentPage', current + 1)"
      >
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/>
        </svg>
      </button>
    </div>
    
    <div class="page-dots">
      <div 
        v-for="page in Math.min(total, 10)" 
        :key="page" 
        :class="['dot', { active: page - 1 === current }]"
        @click="$emit('update:currentPage', page - 1)"
      ></div>
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
  gap: 16px;
  padding: 12px 24px;
  background: var(--surface);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-1);
}

.progress-track {
  flex: 1;
  height: 4px;
  background: var(--surface-3);
  border-radius: 2px;
  overflow: hidden;
}

.track-fill {
  height: 100%;
  background: var(--primary);
  border-radius: 2px;
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.progress-controls {
  display: flex;
  align-items: center;
  gap: 8px;
}

.control-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  background: transparent;
  color: var(--text-secondary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.control-btn:hover:not(:disabled) {
  background: var(--surface-2);
  color: var(--text-primary);
}

.control-btn:active:not(:disabled) {
  background: var(--surface-3);
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
  color: var(--text-disabled);
}

.page-dots {
  display: flex;
  gap: 6px;
  align-items: center;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--surface-3);
  cursor: pointer;
  transition: all 0.2s ease;
}

.dot:hover {
  background: var(--text-disabled);
}

.dot.active {
  background: var(--primary);
  width: 24px;
  border-radius: 4px;
}

@media (max-width: 768px) {
  .progress-bar {
    padding: 8px 16px;
  }
  
  .page-dots {
    display: none;
  }
}
</style>