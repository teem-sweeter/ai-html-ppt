<template>
  <div class="slide sc">
    <div class="section-label" style="color:var(--orange)">03 / 经典激活函数</div>
    <div class="big">Tanh — <span class="hl-orange">零中心的改进</span></div>
    <div class="content">
      <div class="formula">
        <div class="formula-name" style="color:var(--orange)">tanh(x) = (e<sup>x</sup> − e<sup>−x</sup>) / (e<sup>x</sup> + e<sup>−x</sup>)</div>
        <div class="formula-desc">
          <p>将输入映射到(-1,1)区间，零中心化输出。</p>
          <p>优点：输出零中心，梯度更强。</p>
          <p>缺点：仍然存在梯度消失问题。</p>
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

.hl-orange {
  color: var(--accent-3);
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