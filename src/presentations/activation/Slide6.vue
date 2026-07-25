<template>
  <div class="slide sc">
    <div class="section-label" style="color:var(--accent-3)">06 / 现代激活函数</div>
    <div class="big">GELU & Swish — <span class="hl-green">Transformer 时代的宠儿</span></div>
    <div class="content">
      <div class="modern-functions">
        <div class="function-card">
          <div class="function-name" style="color:var(--accent)">GELU</div>
          <div class="function-formula">GELU(x) = x · Φ(x)</div>
          <div class="function-desc">
            <p>其中 Φ(x) 是标准正态分布的累积分布函数。</p>
            <p><strong>使用场景</strong>：BERT、GPT、ViT 等 Transformer 架构的标配</p>
          </div>
        </div>
        <div class="function-card">
          <div class="function-name" style="color:var(--green)">Swish</div>
          <div class="function-formula">Swish(x) = x · σ(x)</div>
          <div class="function-desc">
            <p>其中 σ(x) 是 Sigmoid 函数。</p>
            <p><strong>使用场景</strong>：EfficientNet、MobileNet 等高效网络</p>
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

.hl-green {
  color: var(--green);
}

.content {
  width: 100%;
  max-width: 1100px;
}

.modern-functions {
  display: flex;
  gap: 24px;
}

.function-card {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
  border-top: 3px solid var(--accent);
}

.function-name {
  font-family: 'JetBrains Mono', monospace;
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 12px;
}

.function-formula {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  color: var(--text-primary);
  margin-bottom: 12px;
  padding: 8px;
  background: var(--surface-2);
  border-radius: 4px;
}

.function-desc p {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
  margin-bottom: 8px;
}
</style>