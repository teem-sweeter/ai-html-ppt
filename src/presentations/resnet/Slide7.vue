<template>
  <div class="slide slide-content">
    <div class="section-label">07 / 为什么有效</div>
    <div class="big-text">梯度的<span class="highlight-green">高速公路</span></div>
    <p class="desc-text">
      残差连接为梯度反向传播提供了一条"捷径"，让梯度可以直接从深层传回浅层，
      有效缓解梯度消失问题。
    </p>
    <div class="content">
      <div class="gradient-flow">
        <div class="flow-item">
          <h3 style="color:#ff6b6b">没有残差连接</h3>
          <div class="formula">∂L/∂x = ∂L/∂y · ∂h₁/∂x · ∂h₂/∂h₁ · ... · ∂y/∂hₙ</div>
          <p>每一项 &lt; 1 时，连乘 → 0（梯度消失）<br>
          每一项 &gt; 1 时，连乘 → ∞（梯度爆炸）</p>
        </div>
        <div class="flow-item">
          <h3 style="color:var(--green)">有残差连接</h3>
          <div class="formula">∂L/∂x = ∂L/∂y · (1 + ∂F/∂x)</div>
          <p>梯度可以直接传回（+1项），缓解梯度消失。</p>
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

.highlight-green {
  color: var(--green);
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

.gradient-flow {
  display: flex;
  gap: 24px;
}

.flow-item {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
}

.flow-item h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 16px;
}

.formula {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  color: var(--text-primary);
  background: var(--surface-2);
  padding: 16px;
  border-radius: 4px;
  margin-bottom: 16px;
  overflow-x: auto;
}

.flow-item p {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
}
</style>