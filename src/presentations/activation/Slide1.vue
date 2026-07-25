<template>
  <div class="slide sc">
    <div class="section-label" style="color:var(--accent)">01 / 核心概念</div>
    <div class="big">什么是激活函数？为什么需要它？</div>
    <p class="desc">
      激活函数是神经网络中每个神经元的"开关"——它接收输入的加权求和，经过一个非线性函数变换后输出。
      没有它，无论网络多少层，最终都只是一个线性变换。
    </p>
    <div class="cards">
      <div class="card">
        <div class="card-top" style="background:var(--accent)"></div>
        <h3>神经元的运作</h3>
        <p>输入 → 加权求和 → 激活函数 → 输出</p>
      </div>
      <div class="card">
        <div class="card-top" style="background:var(--accent-2)"></div>
        <h3>直觉理解</h3>
        <p>就像大脑神经元：只有当输入信号足够强（超过某个阈值）时，神经元才会"激活"并向下传递信号。</p>
      </div>
      <div class="card">
        <div class="card-top" style="background:var(--accent-3)"></div>
        <h3>为什么不能没有激活函数？</h3>
        <p>没有激活函数，多层网络等价于单层线性变换，无法学习复杂模式。</p>
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

.desc {
  font-size: 18px;
  line-height: 1.8;
  color: var(--text-muted);
  max-width: 800px;
  margin-bottom: 40px;
}

.cards {
  display: flex;
  gap: 24px;
  width: 100%;
  max-width: 1100px;
}

.card {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 24px;
  position: relative;
  overflow: hidden;
}

.card-top {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
}

.card h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 12px;
  color: var(--text-primary);
}

.card p {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-muted);
}
</style>