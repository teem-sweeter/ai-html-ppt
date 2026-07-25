<template>
  <div class="slide slide-calc">
    <div class="calc-header">
      <span class="step-badge">STEP 4 / 4</span>
      <h2>右下区域（行2-3，列2-3）</h2>
    </div>
    <div class="calc-body">
      <div class="grid-wrapper">
        <div class="grid-label">输入特征图 4×4</div>
        <div class="matrix-4x4">
          <div class="matrix-cell dim-cell">1</div>
          <div class="matrix-cell dim-cell">3</div>
          <div class="matrix-cell dim-cell">2</div>
          <div class="matrix-cell dim-cell">4</div>
          <div class="matrix-cell dim-cell">5</div>
          <div class="matrix-cell dim-cell">6</div>
          <div class="matrix-cell dim-cell">1</div>
          <div class="matrix-cell dim-cell">0</div>
          <div class="matrix-cell dim-cell">2</div>
          <div class="matrix-cell dim-cell">1</div>
          <div class="matrix-cell active-cell">7</div>
          <div class="matrix-cell active-cell">3</div>
          <div class="matrix-cell dim-cell">8</div>
          <div class="matrix-cell dim-cell">4</div>
          <div class="matrix-cell max-cell">9</div>
          <div class="matrix-cell active-cell">5</div>
        </div>
      </div>
      <div class="arrow-section">
        <div class="arrow-line"></div>
      </div>
      <div class="grid-wrapper">
        <div class="grid-label">输出特征图 2×2</div>
        <div class="matrix-2x2">
          <div class="matrix-cell" style="opacity:0.4; color:var(--accent)">6</div>
          <div class="matrix-cell" style="opacity:0.4; color:var(--accent)">4</div>
          <div class="matrix-cell" style="opacity:0.4; color:var(--accent)">8</div>
          <div class="matrix-cell result-new">9</div>
        </div>
      </div>
      <div class="formula-section">
        <div class="formula-title">COMPUTATION</div>
        <div class="formula-values">
          <span class="formula-val" style="color:var(--highlight); border-color:var(--highlight)">7</span>
          <span class="formula-val">3</span>
          <span class="formula-val" style="color:var(--highlight); border-color:var(--highlight)">9</span>
          <span class="formula-val">5</span>
        </div>
        <div class="formula-result">
          max(7, 3, 9, 5) = <strong>9</strong><br><br>
          result[1][1] = <strong>9</strong>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.slide-calc {
  background: var(--bg);
  align-items: flex-start;
}

.calc-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 40px;
}

.step-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  font-weight: 700;
  background: var(--accent);
  color: var(--bg);
  padding: 5px 14px;
  border-radius: 2px;
  white-space: nowrap;
}

.calc-header h2 {
  font-size: clamp(24px, 3.5vw, 40px);
  font-weight: 900;
}

.calc-body {
  display: flex;
  gap: 48px;
  width: 100%;
  max-width: 1100px;
  align-items: center;
}

.grid-wrapper {
  flex-shrink: 0;
}

.grid-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  margin-bottom: 12px;
}

.matrix-4x4 {
  display: grid;
  grid-template-columns: repeat(4, 64px);
  grid-template-rows: repeat(4, 64px);
  gap: 3px;
}

.matrix-cell {
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 20px;
  font-weight: 700;
  background: var(--grid-cell);
  border: 1px solid var(--grid-border);
  border-radius: 3px;
  transition: all 0.4s ease;
  position: relative;
}

.matrix-cell.active-cell {
  background: rgba(0, 229, 255, 0.12);
  border-color: var(--accent);
  color: var(--accent);
  box-shadow: 0 0 20px rgba(0, 229, 255, 0.15);
}

.matrix-cell.max-cell {
  background: rgba(255, 171, 0, 0.2);
  border-color: var(--highlight);
  color: var(--highlight);
  box-shadow: 0 0 24px rgba(255, 171, 0, 0.2);
  z-index: 2;
}

.matrix-cell.dim-cell {
  opacity: 0.2;
}

.arrow-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  flex-shrink: 0;
}

.arrow-line {
  width: 60px;
  height: 2px;
  background: linear-gradient(90deg, var(--accent), var(--accent-2));
  position: relative;
}

.arrow-line::after {
  content: '';
  position: absolute;
  right: -2px;
  top: -6px;
  border: 7px solid transparent;
  border-left: 10px solid var(--accent-2);
}

.matrix-2x2 {
  display: grid;
  grid-template-columns: repeat(2, 80px);
  grid-template-rows: repeat(2, 80px);
  gap: 4px;
}

.matrix-2x2 .matrix-cell {
  font-size: 28px;
  background: var(--surface-2);
  border-color: var(--grid-border);
  transition: all 0.4s ease;
}

.matrix-2x2 .matrix-cell.result-new {
  background: rgba(255, 171, 0, 0.15);
  border-color: var(--highlight);
  color: var(--highlight);
  box-shadow: 0 0 20px rgba(255, 171, 0, 0.15);
}

.formula-section {
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px 32px;
  max-width: 420px;
  flex: 1;
}

.formula-title {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.15em;
  color: var(--accent);
  margin-bottom: 16px;
}

.formula-values {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 16px;
}

.formula-val {
  font-family: 'JetBrains Mono', monospace;
  font-size: 20px;
  font-weight: 700;
  background: var(--grid-cell);
  border: 1px solid var(--grid-border);
  padding: 8px 16px;
  border-radius: 4px;
  color: var(--accent);
}

.formula-result {
  font-family: 'JetBrains Mono', monospace;
  font-size: 15px;
  color: var(--text-muted);
  line-height: 1.8;
}

.formula-result strong {
  color: var(--highlight);
  font-size: 22px;
}
</style>