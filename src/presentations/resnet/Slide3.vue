<template>
  <div class="slide slide-content">
    <div class="section-label">03 / 残差块结构</div>
    <div class="big-text">残差块 (Residual Block) <span class="highlight">解剖图</span></div>
    <div class="content">
      <div class="block-structure">
        <div class="block-diagram">
          <div class="block-title">残差块结构</div>
          <div class="diagram">
            <div class="layer">Input (x)</div>
            <div class="arrow">↓</div>
            <div class="layer">Conv → BN → ReLU</div>
            <div class="arrow">↓</div>
            <div class="layer">Conv → BN</div>
            <div class="arrow">↓</div>
            <div class="addition">+ (残差连接)</div>
            <div class="arrow">↓</div>
            <div class="layer">ReLU</div>
            <div class="arrow">↓</div>
            <div class="layer">Output</div>
          </div>
        </div>
        <div class="block-desc">
          <h3>关键组件</h3>
          <ul>
            <li><strong>跳跃连接 (Skip Connection)</strong>：直接将输入加到输出上</li>
            <li><strong>恒等映射</strong>：当维度匹配时，直接使用输入</li>
            <li><strong>投影快捷连接</strong>：当维度不匹配时，使用1x1卷积调整维度</li>
          </ul>
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

.block-structure {
  display: flex;
  gap: 40px;
}

.block-diagram {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
}

.block-title {
  font-family: 'JetBrains Mono', monospace;
  font-size: 16px;
  font-weight: 700;
  color: var(--accent);
  margin-bottom: 20px;
  text-align: center;
}

.diagram {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.layer {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  color: var(--text-primary);
  background: var(--surface-2);
  padding: 8px 16px;
  border-radius: 4px;
  width: 100%;
  text-align: center;
}

.arrow {
  color: var(--accent);
  font-size: 18px;
}

.addition {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  color: var(--green);
  background: rgba(0, 230, 118, 0.1);
  padding: 8px 16px;
  border-radius: 4px;
  width: 100%;
  text-align: center;
  border: 1px solid var(--green);
}

.block-desc {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
}

.block-desc h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 16px;
  color: var(--text-primary);
}

.block-desc ul {
  list-style: none;
  padding: 0;
}

.block-desc li {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
  margin-bottom: 12px;
  padding-left: 20px;
  position: relative;
}

.block-desc li::before {
  content: '•';
  color: var(--accent);
  position: absolute;
  left: 0;
}
</style>