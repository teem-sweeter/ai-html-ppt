<template>
  <div class="slide sc">
    <div class="section-label" style="color:var(--accent)">07 / 全面对比</div>
    <div class="big">激活函数<span class="hl">横向对比</span></div>
    <div class="content">
      <div class="comparison">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>函数</th>
              <th>值域</th>
              <th>零中心</th>
              <th>梯度消失</th>
              <th>计算速度</th>
              <th>典型应用</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="color:var(--yellow)">Sigmoid</td>
              <td>(0,1)</td>
              <td>否</td>
              <td>严重</td>
              <td>中等</td>
              <td>二分类输出层</td>
            </tr>
            <tr>
              <td style="color:var(--orange)">Tanh</td>
              <td>(-1,1)</td>
              <td>是</td>
              <td>中等</td>
              <td>中等</td>
              <td>RNN、LSTM</td>
            </tr>
            <tr>
              <td style="color:var(--accent)">ReLU</td>
              <td>[0,+∞)</td>
              <td>否</td>
              <td>无（正值）</td>
              <td>快</td>
              <td>CNN默认选择</td>
            </tr>
            <tr>
              <td style="color:var(--accent-2)">GELU</td>
              <td>≈(-0.17,+∞)</td>
              <td>近似</td>
              <td>无</td>
              <td>较慢</td>
              <td>Transformer</td>
            </tr>
          </tbody>
        </table>
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

.hl {
  color: var(--accent);
}

.content {
  width: 100%;
  max-width: 1100px;
}

.comparison {
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
  overflow-x: auto;
}

.comparison-table {
  width: 100%;
  border-collapse: collapse;
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
}

.comparison-table th,
.comparison-table td {
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid var(--grid-border);
}

.comparison-table th {
  color: var(--text-primary);
  font-weight: 700;
  background: var(--surface-2);
}

.comparison-table td {
  color: var(--text-muted);
}

.comparison-table tr:last-child td {
  border-bottom: none;
}
</style>