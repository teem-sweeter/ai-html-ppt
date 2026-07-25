<template>
  <div class="slide sc">
    <div class="section-label" style="color:var(--accent-3)">08 / 实践指南</div>
    <div class="big">如何选择激活函数？</div>
    <div class="content">
      <div class="guidelines">
        <div class="guideline" style="border-left:3px solid var(--accent)">
          <h3>CNN 图像任务</h3>
          <p><strong>ReLU</strong> 仍然是安全的默认选择。追求更好效果时试 <strong>Swish</strong>。</p>
        </div>
        <div class="guideline" style="border-left:3px solid var(--accent-2)">
          <h3>Transformer / NLP</h3>
          <p><strong>GELU</strong> 是标准选择（BERT、GPT 系列均使用）。</p>
        </div>
        <div class="guideline" style="border-left:3px solid var(--accent-3)">
          <h3>输出层</h3>
          <p>二分类 → <strong>Sigmoid</strong><br>多分类 → <strong>Softmax</strong><br>回归 → 无激活 / 线性</p>
        </div>
        <div class="guideline" style="border-left:3px solid var(--green)">
          <h3>隐藏层</h3>
          <p>首选 <strong>ReLU</strong> 或 <strong>GELU</strong>，避免 Sigmoid/Tanh。</p>
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

.guidelines {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.guideline {
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 20px 24px;
}

.guideline h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--text-primary);
}

.guideline p {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
}
</style>