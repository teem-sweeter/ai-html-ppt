<template>
  <div class="slide slide-content">
    <div class="section-label">08 / 实验结果</div>
    <div class="big-text">ImageNet 上的<span class="highlight">统治级</span>表现</div>
    <div class="content">
      <div class="results">
        <div class="result-item">
          <div class="result-number" style="color:var(--accent)">3.57%</div>
          <div class="result-label">Top-5 Error</div>
          <div class="result-desc">ResNet-152 在 ImageNet 上达到 3.57% top-5 错误率，超越人类水平（约5.1%）。</div>
        </div>
        <div class="result-item">
          <div class="result-number" style="color:var(--accent-3)">1st</div>
          <div class="result-label">ILSVRC 2015</div>
          <div class="result-desc">横扫 ImageNet 分类、检测、定位三项冠军，奠定深度残差学习的里程碑地位。</div>
        </div>
        <div class="result-item">
          <div class="result-number" style="color:var(--accent-2)">1000+</div>
          <div class="result-label">可训练深度</div>
          <div class="result-desc">理论上残差网络可以扩展到 1000 层以上仍然可训练，彻底突破了深度瓶颈。</div>
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
  font-size: clamp(24px, 3vw, 38px);
  font-weight: 900;
  margin-bottom: 24px;
  line-height: 1.2;
}

.highlight {
  color: var(--accent);
}

.content {
  width: 100%;
  max-width: 1100px;
}

.results {
  display: flex;
  gap: 24px;
}

.result-item {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
  text-align: center;
}

.result-number {
  font-family: 'JetBrains Mono', monospace;
  font-size: 48px;
  font-weight: 900;
  margin-bottom: 8px;
}

.result-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 16px;
}

.result-desc {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
}
</style>