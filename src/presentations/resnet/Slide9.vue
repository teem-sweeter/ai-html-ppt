<template>
  <div class="slide slide-content">
    <div class="section-label">09 / 总结</div>
    <div class="big-text">ResNet 带来了什么？</div>
    <div class="content">
      <div class="summary">
        <div class="summary-item">
          <div class="summary-icon">F</div>
          <div>
            <h3>残差学习</h3>
            <p>学习 F(x) = H(x) − x，而非直接学 H(x)。让恒等映射变得容易学习，解决退化问题。</p>
          </div>
        </div>
        <div class="summary-item">
          <div class="summary-icon">+</div>
          <div>
            <h3>跳跃连接</h3>
            <p>shortcut connection 直接传递输入，梯度有了"高速公路"，训练数百层成为可能。</p>
          </div>
        </div>
        <div class="summary-item">
          <div class="summary-icon">∞</div>
          <div>
            <h3>深度突破</h3>
            <p>从几十层到上千层，ResNet 打破了深度网络的训练瓶颈，开启了超深网络时代。</p>
          </div>
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
  font-size: clamp(24px, 3.5vw, 44px);
  font-weight: 900;
  margin-bottom: 24px;
  line-height: 1.2;
}

.content {
  width: 100%;
  max-width: 1100px;
}

.summary {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.summary-item {
  display: flex;
  gap: 20px;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
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
  font-weight: 900;
}

.summary-item h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--text-primary);
}

.summary-item p {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
}
</style>