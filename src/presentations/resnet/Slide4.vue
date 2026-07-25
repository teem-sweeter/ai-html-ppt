<template>
  <div class="slide slide-content">
    <div class="section-label">04 / 数学表达</div>
    <div class="big-text">残差学习的数学本质</div>
    <div class="content">
      <div class="math-section">
        <div class="formula-box">
          <div class="formula-main">
            y = F(x, {W<sub>i</sub>}) + x
          </div>
          <div class="formula-note">
            x：输入（恒等映射）<br>
            F(x)：残差函数（要学习的部分）<br>
            y：输出
          </div>
        </div>
        <div class="explanation">
          <h3>关键洞察</h3>
          <p>如果最优映射接近恒等映射（H(x) ≈ x），那么残差 F(x) = H(x) - x ≈ 0，
          比直接学习 H(x) = x 容易得多。</p>
          <p>这就是为什么ResNet能够训练上千层的网络。</p>
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

.content {
  width: 100%;
  max-width: 1100px;
}

.math-section {
  display: flex;
  gap: 24px;
}

.formula-box {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
}

.formula-main {
  font-family: 'JetBrains Mono', monospace;
  font-size: 28px;
  font-weight: 700;
  color: var(--text-primary);
  text-align: center;
  margin-bottom: 20px;
  padding: 20px;
  background: var(--surface-2);
  border-radius: 4px;
}

.formula-note {
  font-size: 14px;
  line-height: 1.8;
  color: var(--text-muted);
}

.explanation {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
}

.explanation h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 16px;
  color: var(--text-primary);
}

.explanation p {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
  margin-bottom: 12px;
}
</style>