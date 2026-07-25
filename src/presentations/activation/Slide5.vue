<template>
  <div class="slide sc">
    <div class="section-label" style="color:var(--purple)">05 / ReLU 变体</div>
    <div class="big">解决 Dead ReLU 的<span class="hl-purple">三种方案</span></div>
    <div class="content">
      <div class="variants">
        <div class="variant">
          <div class="variant-name" style="color:var(--purple)">Leaky ReLU</div>
          <div class="variant-formula">f(x) = max(0.01x, x)</div>
          <div class="variant-desc">负值区域有小的斜率，避免神经元死亡。</div>
        </div>
        <div class="variant">
          <div class="variant-name" style="color:var(--green)">ELU</div>
          <div class="variant-formula">f(x) = x if x > 0, α(eˣ - 1) if x ≤ 0</div>
          <div class="variant-desc">指数线性单元，输出均值更接近零。</div>
        </div>
        <div class="variant">
          <div class="variant-name" style="color:var(--accent)">GELU</div>
          <div class="variant-formula">f(x) = x · Φ(x)</div>
          <div class="variant-desc">高斯误差线性单元，Transformer的标配。</div>
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

.hl-purple {
  color: var(--accent-2);
}

.content {
  width: 100%;
  max-width: 1100px;
}

.variants {
  display: flex;
  gap: 24px;
}

.variant {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
}

.variant-name {
  font-family: 'JetBrains Mono', monospace;
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 12px;
}

.variant-formula {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  color: var(--text-primary);
  margin-bottom: 12px;
  padding: 8px;
  background: var(--surface-2);
  border-radius: 4px;
}

.variant-desc {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
}
</style>