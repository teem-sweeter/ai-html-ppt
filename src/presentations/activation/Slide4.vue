<template>
  <div class="slide sc">
    <div class="section-label" style="color:var(--accent)">04 / 现代标准</div>
    <div class="big">ReLU — <span class="hl">深度学习的默认选择</span></div>
    <div class="content">
      <div class="formula">
        <div class="formula-name" style="color:var(--accent)">ReLU(x) = max(0, x)</div>
        <div class="formula-desc">
          <p>现代深度学习最常用的激活函数。</p>
          <p>优点：计算简单，缓解梯度消失。</p>
          <p>缺点：死亡ReLU问题（负值区域梯度为0）。</p>
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

.hl {
  color: var(--accent);
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