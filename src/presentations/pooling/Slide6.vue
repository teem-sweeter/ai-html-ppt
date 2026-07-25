<template>
  <div class="slide slide-final">
    <h2>计算完成 — 最终结果</h2>
    <div class="final-layout">
      <div class="final-4x4">
        <div class="grid-label">输入 4×4</div>
        <div class="matrix-4x4" style="margin-top:12px">
          <div class="matrix-cell" style="background:rgba(0,229,255,0.06); border-color:rgba(0,229,255,0.2)">1</div>
          <div class="matrix-cell" style="background:rgba(0,229,255,0.06); border-color:rgba(0,229,255,0.2)">3</div>
          <div class="matrix-cell" style="background:rgba(124,77,255,0.06); border-color:rgba(124,77,255,0.2)">2</div>
          <div class="matrix-cell" style="background:rgba(124,77,255,0.06); border-color:rgba(124,77,255,0.2)">4</div>
          <div class="matrix-cell" style="background:rgba(0,229,255,0.06); border-color:rgba(0,229,255,0.2)">5</div>
          <div class="matrix-cell max-cell">6</div>
          <div class="matrix-cell" style="background:rgba(124,77,255,0.06); border-color:rgba(124,77,255,0.2)">1</div>
          <div class="matrix-cell max-cell" style="background:rgba(124,77,255,0.2); border-color:var(--accent-2); color:var(--accent-2)">4</div>
          <div class="matrix-cell" style="background:rgba(0,230,118,0.06); border-color:rgba(0,230,118,0.2)">2</div>
          <div class="matrix-cell" style="background:rgba(0,230,118,0.06); border-color:rgba(0,230,118,0.2)">1</div>
          <div class="matrix-cell" style="background:rgba(255,109,0,0.06); border-color:rgba(255,109,0,0.2)">7</div>
          <div class="matrix-cell" style="background:rgba(255,109,0,0.06); border-color:rgba(255,109,0,0.2)">3</div>
          <div class="matrix-cell max-cell" style="background:rgba(0,230,118,0.2); border-color:var(--green); color:var(--green)">8</div>
          <div class="matrix-cell" style="background:rgba(0,230,118,0.06); border-color:rgba(0,230,118,0.2)">4</div>
          <div class="matrix-cell max-cell" style="background:rgba(255,109,0,0.2); border-color:var(--accent-3); color:var(--accent-3)">9</div>
          <div class="matrix-cell" style="background:rgba(255,109,0,0.06); border-color:rgba(255,109,0,0.2)">5</div>
        </div>
      </div>
      <div class="arrow-section">
        <div class="arrow-line" style="width:80px"></div>
      </div>
      <div class="final-2x2">
        <div class="grid-label">输出 2×2</div>
        <div class="matrix-2x2" style="margin-top:12px">
          <div class="matrix-cell result-new">6</div>
          <div class="matrix-cell result-new">4</div>
          <div class="matrix-cell result-new">8</div>
          <div class="matrix-cell result-new">9</div>
        </div>
      </div>
    </div>
    <p class="final-note">
      空间尺寸从 <strong>4×4</strong> 压缩为 <strong>2×2</strong>，通道数不变 — 每个窗口取最大值，保留最强激活信号
    </p>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.slide-final {
  background: radial-gradient(ellipse at 50% 50%, rgba(255, 171, 0, 0.05) 0%, transparent 60%),
              var(--bg);
  text-align: center;
}

.slide-final h2 {
  font-size: clamp(32px, 4vw, 52px);
  font-weight: 900;
  margin-bottom: 48px;
}

.final-layout {
  display: flex;
  align-items: center;
  gap: 60px;
}

.final-4x4 .matrix-4x4 {
  grid-template-columns: repeat(4, 72px);
  grid-template-rows: repeat(4, 72px);
}

.final-2x2 .matrix-2x2 {
  grid-template-columns: repeat(2, 100px);
  grid-template-rows: repeat(2, 100px);
}

.final-2x2 .matrix-cell {
  font-size: 36px;
  background: rgba(255, 171, 0, 0.12);
  border-color: var(--highlight);
  color: var(--highlight);
  box-shadow: 0 0 30px rgba(255, 171, 0, 0.12);
}

.final-note {
  margin-top: 40px;
  font-size: 15px;
  color: var(--text-muted);
  font-weight: 300;
}

.final-note strong {
  color: var(--highlight);
  font-size: 18px;
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

.matrix-cell.max-cell {
  background: rgba(255, 171, 0, 0.2);
  border-color: var(--highlight);
  color: var(--highlight);
  box-shadow: 0 0 24px rgba(255, 171, 0, 0.2);
  z-index: 2;
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
</style>