<template>
  <div class="slide slide-content">
    <div class="section-label">01 / 问题背景</div>
    <div class="big-text">更深的网络，<span class="highlight-danger">反而更差？</span></div>
    <p class="desc-text">
      直觉上，更深的神经网络应该能学习更复杂的特征，表现更好。但实验发现，
      当网络层数增加到一定程度后，训练误差反而上升了——
      这不是过拟合（测试误差也在上升），而是训练本身变得更困难。
    </p>
    <div class="content">
      <div class="problem">
        <div class="problem-title">TRAINING ERROR vs NETWORK DEPTH</div>
        <div class="problem-desc">
          <p>随着网络深度增加，训练误差不降反升，这就是<strong>退化问题</strong>。</p>
          <p>根本原因：梯度消失/爆炸，使得深层网络难以训练。</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.slide-content {
  background: var(--bg);
  align-items: flex-start;
}

.section-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.15em;
  color: var(--accent);
  margin-bottom: 16px;
  opacity: 0.8;
}

.big-text {
  font-size: clamp(32px, 4.5vw, 56px);
  font-weight: 900;
  margin-bottom: 24px;
  line-height: 1.2;
}

.highlight-danger {
  color: #ff6b6b;
}

.desc-text {
  font-size: 18px;
  line-height: 1.8;
  color: var(--text-muted);
  max-width: 800px;
  margin-bottom: 40px;
}

.content {
  width: 100%;
  max-width: 1100px;
}

.problem {
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
}

.problem-title {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  font-weight: 700;
  color: var(--accent);
  margin-bottom: 16px;
}

.problem-desc p {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
  margin-bottom: 12px;
}
</style>