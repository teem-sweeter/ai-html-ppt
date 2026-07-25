<template>
  <div class="slide sc">
    <div class="section-label" style="color:var(--yellow)">02 / 经典激活函数</div>
    <div class="big">Sigmoid — <span class="hl-yellow">最早的激活函数</span></div>
    <div class="content">
      <div class="formula">
        <div class="formula-name" style="color:var(--yellow)">σ(x) = 1 / (1 + e<sup>−x</sup>)</div>
        <div class="formula-desc">
          <p>将任意输入映射到(0,1)区间，常用于二分类输出层。</p>
          <p>优点：输出范围有界，便于解释。</p>
          <p>缺点：梯度消失问题，输出非零中心。</p>
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

.hl-yellow {
  color: var(--highlight);
}

.content {
  width: 100%;
  max-width: 1100px;
}

.formula {
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 32px;
}

.formula-name {
  font-family: 'JetBrains Mono', monospace;
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 24px;
}

.formula-desc p {
  font-size: 16px;
  line-height: 1.8;
  color: var(--text-muted);
  margin-bottom: 12px;
}
</style>