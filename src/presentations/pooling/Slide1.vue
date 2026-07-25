<template>
  <div class="slide slide-concept">
    <div class="section-tag">01 / 核心概念</div>
    <h2>什么是池化？</h2>
    <div class="concept-grid">
      <div class="concept-card">
        <div class="num">01</div>
        <h3>下采样操作</h3>
        <p>池化在空间维度上对特征图进行压缩，用一个值来概括局部区域的信息，将一小块区域"浓缩"成一个值。</p>
      </div>
      <div class="concept-card">
        <div class="num">02</div>
        <h3>降低计算量</h3>
        <p>特征图尺寸缩小后，后续层的参数和计算量大幅减少，提升网络运行效率。</p>
      </div>
      <div class="concept-card">
        <div class="num">03</div>
        <h3>提取主要特征</h3>
        <p>保留最突出的信息，过滤掉不重要的细节，提取局部最显著的特征响应。</p>
      </div>
      <div class="concept-card">
        <div class="num">04</div>
        <h3>平移不变性</h3>
        <p>特征位置稍有偏移时，池化后的结果变化不大，增强模型对位置变化的鲁棒性。</p>
      </div>
    </div>
    <div class="pool-type-row">
      <div class="pool-type-badge">Max Pooling — 最大池化</div>
      <div class="pool-type-badge">Average Pooling — 平均池化</div>
      <div class="pool-type-badge">Global Avg Pooling — 全局平均池化</div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.slide-concept {
  background: radial-gradient(ellipse at 20% 80%, rgba(124, 77, 255, 0.06) 0%, transparent 50%),
              var(--bg);
  align-items: flex-start;
}

.slide-concept .section-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.15em;
  color: var(--accent-2);
  margin-bottom: 16px;
  opacity: 0.8;
}

.slide-concept h2 {
  font-size: clamp(32px, 4.5vw, 56px);
  font-weight: 900;
  margin-bottom: 48px;
  line-height: 1.2;
}

.concept-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  width: 100%;
  max-width: 1100px;
}

.concept-card {
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 32px;
  position: relative;
  overflow: hidden;
  opacity: 0;
  transform: translateY(20px);
}

.slide-concept.active .concept-card {
  animation: fadeUp 0.5s ease forwards;
}
.slide-concept.active .concept-card:nth-child(2) { animation-delay: 0.1s; }
.slide-concept.active .concept-card:nth-child(3) { animation-delay: 0.2s; }
.slide-concept.active .concept-card:nth-child(4) { animation-delay: 0.3s; }

@keyframes fadeUp {
  to { opacity: 1; transform: translateY(0); }
}

.concept-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
}

.concept-card:nth-child(1)::before { background: var(--accent); }
.concept-card:nth-child(2)::before { background: var(--accent-2); }
.concept-card:nth-child(3)::before { background: var(--green); }
.concept-card:nth-child(4)::before { background: var(--accent-3); }

.concept-card .num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 42px;
  font-weight: 700;
  opacity: 0.08;
  position: absolute;
  top: 12px;
  right: 20px;
}

.concept-card h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 10px;
  color: var(--text-primary);
}

.concept-card p {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
}

.pool-type-row {
  display: flex;
  gap: 16px;
  margin-top: 48px;
  flex-wrap: wrap;
}

.pool-type-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  padding: 8px 16px;
  background: var(--surface-2);
  border: 1px solid var(--grid-border);
  border-radius: 4px;
  color: var(--text-muted);
}
</style>