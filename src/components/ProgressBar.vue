<template>
  <div class="progress-bar">
    <button class="nav-btn" :disabled="current === 0" @click="$emit('update:currentPage', current - 1)">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
        <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
      </svg>
    </button>
    
    <div class="dots">
      <div 
        v-for="page in total" 
        :key="page" 
        :class="['dot', { active: page - 1 === current }]"
        @click="$emit('update:currentPage', page - 1)"
      ></div>
    </div>
    
    <button class="nav-btn" :disabled="current === total - 1" @click="$emit('update:currentPage', current + 1)">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
        <path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/>
      </svg>
    </button>
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
  position: fixed;
  bottom: 0;
  left: 280px;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 12px 0;
  background: rgba(30, 30, 30, 0.95);
  backdrop-filter: blur(10px);
  z-index: 50;
}

.nav-btn {
  width: 28px;
  height: 28px;
  border: none;
  background: transparent;
  color: rgba(255, 255, 255, 0.5);
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s ease;
}

.nav-btn:hover:not(:disabled) {
  color: white;
  background: rgba(255, 255, 255, 0.1);
}

.nav-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.dots {
  display: flex;
  gap: 6px;
  align-items: center;
}

.dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  cursor: pointer;
  transition: all 0.2s ease;
}

.dot:hover {
  background: rgba(255, 255, 255, 0.4);
}

.dot.active {
  background: white;
  width: 18px;
  border-radius: 3px;
}
</style>