<template>
  <div class="slide slide-summary">
    <div class="section-tag">02 / 总结</div>
    <h2>池化的核心作用</h2>
    <div class="summary-grid">
      <div class="summary-item">
        <div class="summary-icon">↓</div>
        <div>
          <h3>降低计算量</h3>
          <p>特征图尺寸缩小，后续层的参数和计算量大幅减少，提升网络训练和推理效率。</p>
        </div>
      </div>
      <div class="summary-item">
        <div class="summary-icon">◎</div>
        <div>
          <h3>提取主要特征</h3>
          <p>保留最显著的激活响应，过滤掉次要信息，聚焦于局部区域中最突出的特征。</p>
        </div>
      </div>
      <div class="summary-item">
        <div class="summary-icon">↔</div>
        <div>
          <h3>增强平移不变性</h3>
          <p>特征位置稍有偏移时，池化后的输出变化不大，让模型对位置变化更加鲁棒。</p>
        </div>
      </div>
      <div class="summary-item">
        <div class="summary-icon">◇</div>
        <div>
          <h3>防止过拟合</h3>
          <p>减少参数量，降低模型复杂度，减少过拟合风险，提升模型泛化能力。</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.slide-summary {
  background: var(--bg);
  align-items: flex-start;
}

.slide-summary .section-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.15em;
  color: var(--accent-2);
  margin-bottom: 16px;
  opacity: 0.8;
}

.slide-summary h2 {
  font-size: clamp(32px, 4.5vw, 56px);
  font-weight: 900;
  margin-bottom: 48px;
  line-height: 1.2;
}

.summary-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  width: 100%;
  max-width: 1100px;
}

.summary-item {
  display: flex;
  gap: 20px;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 32px;
  opacity: 0;
  transform: translateY(20px);
}

.slide-summary.active .summary-item {
  animation: fadeUp 0.5s ease forwards;
}
.slide-summary.active .summary-item:nth-child(2) { animation-delay: 0.1s; }
.slide-summary.active .summary-item:nth-child(3) { animation-delay: 0.2s; }
.slide-summary.active .summary-item:nth-child(4) { animation-delay: 0.3s; }

@keyframes fadeUp {
  to { opacity: 1; transform: translateY(0); }
}

.summary-icon {
  font-size: 32px;
  color: var(--accent);
  flex-shrink: 0;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 229, 255, 0.1);
  border-radius: 8px;
}

.summary-item h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 10px;
  color: var(--text-primary);
}

.summary-item p {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
}
</style>