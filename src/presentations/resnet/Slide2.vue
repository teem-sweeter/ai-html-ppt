<template>
  <div class="slide slide-content">
    <div class="section-label">02 / 核心思想</div>
    <div class="big-text">如果学习恒等映射很难，<br>那就让它<span class="highlight">变得容易</span></div>
    <p class="desc-text">
      ResNet 的核心洞察：与其让网络直接学习目标映射 H(x)，不如让它学习残差
      F(x) = H(x) − x。这样，如果最优解就是恒等映射，网络只需把 F(x) 学成 0 即可——
      比学习 H(x) = x 容易得多。
    </p>
    <div class="content">
      <div class="comparison">
        <div class="comparison-item">
          <h3 style="color:#ff6b6b">传统网络</h3>
          <div class="formula">x → [层] → H(x)</div>
          <p>直接学习目标映射，难以优化恒等映射。</p>
        </div>
        <div class="comparison-item">
          <h3 style="color:var(--accent)">残差网络</h3>
          <div class="formula">x → [层] → F(x) + x</div>
          <p>学习残差 F(x) = H(x) - x，更容易优化。</p>
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

.highlight {
  color: var(--accent);
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

.comparison {
  display: flex;
  gap: 24px;
}

.comparison-item {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
}

.comparison-item h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 16px;
}

.formula {
  font-family: 'JetBrains Mono', monospace;
  font-size: 18px;
  font-weight: 700;
  color: var(--text-primary);
  background: var(--surface-2);
  padding: 16px;
  border-radius: 4px;
  text-align: center;
  margin-bottom: 16px;
}

.comparison-item p {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
}
</style>