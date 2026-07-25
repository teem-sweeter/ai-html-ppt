<template>
  <div class="slide sc">
    <div class="section-label" style="color:var(--accent)">09 / 总结</div>
    <div class="big">激活函数的演进之路</div>
    <div class="content">
      <div class="summary">
        <div class="summary-item">
          <div class="summary-icon">σ</div>
          <div>
            <h3>非线性是核心</h3>
            <p>没有激活函数，神经网络就是线性变换的堆叠，表达能力极其有限。激活函数赋予了网络拟合任意复杂函数的能力。</p>
          </div>
        </div>
        <div class="summary-item">
          <div class="summary-icon">∇</div>
          <div>
            <h3>梯度是关键约束</h3>
            <p>激活函数的选择直接影响梯度流。Sigmoid/Tanh 的梯度消失催生了 ReLU，ReLU 的 Dead 问题催生了变体。</p>
          </div>
        </div>
        <div class="summary-item">
          <div class="summary-icon">⚡</div>
          <div>
            <h3>实践建议</h3>
            <p>CNN 默认用 ReLU，Transformer 用 GELU，输出层根据任务选择。没有万能的激活函数，只有最适合的。</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.sc {
  background: var(--bg);
  align-items: flex-start;
}

.section-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.15em;
  margin-bottom: 16px;
  opacity: 0.8;
}

.big {
  font-size: clamp(32px, 4.5vw, 56px);
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