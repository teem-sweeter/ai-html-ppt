<template>
  <div class="slide slide-title">
    <div class="tag">Deep Learning · Fundamentals</div>
    <h1>激活函数</h1>
    <p class="subtitle">Activation Functions — 赋予神经网络非线性力量的核心机制</p>
    <div class="hint">按 → 或点击底部导航切换页面</div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.slide-title {
  background: radial-gradient(ellipse at 30% 50%, rgba(0, 229, 255, 0.08) 0%, transparent 60%),
              radial-gradient(ellipse at 70% 30%, rgba(124, 77, 255, 0.06) 0%, transparent 50%),
              var(--bg);
}

.slide-title .tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
  border: 1px solid rgba(0, 229, 255, 0.3);
  padding: 6px 18px;
  border-radius: 2px;
  margin-bottom: 40px;
}

.slide-title h1 {
  font-size: clamp(48px, 7vw, 96px);
  font-weight: 900;
  letter-spacing: -0.02em;
  line-height: 1.1;
  text-align: center;
  margin-bottom: 20px;
  background: linear-gradient(135deg, #ffffff 0%, #b0b8d1 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.slide-title .subtitle {
  font-size: clamp(16px, 2vw, 22px);
  color: var(--text-muted);
  font-weight: 300;
  letter-spacing: 0.05em;
  text-align: center;
}

.slide-title .hint {
  position: absolute;
  bottom: 40px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: var(--text-muted);
  opacity: 0.5;
  animation: pulse 2s ease infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.7; }
}
</style>