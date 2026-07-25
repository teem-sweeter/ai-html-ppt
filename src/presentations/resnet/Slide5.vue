<template>
  <div class="slide slide-content">
    <div class="section-label">05 / 两种残差块</div>
    <div class="big-text">Basic Block vs Bottleneck Block</div>
    <div class="content">
      <div class="comparison">
        <div class="comparison-item" style="border-top:3px solid var(--accent)">
          <h3 style="color:var(--accent)">Basic Block</h3>
          <p class="usage">用于 ResNet-18 / ResNet-34</p>
          <div class="structure">
            <div class="layer">Conv 3×3</div>
            <div class="arrow">→</div>
            <div class="layer">BN → ReLU</div>
            <div class="arrow">→</div>
            <div class="layer">Conv 3×3</div>
            <div class="arrow">→</div>
            <div class="layer">BN</div>
          </div>
        </div>
        <div class="comparison-item" style="border-top:3px solid var(--accent-2)">
          <h3 style="color:var(--accent-2)">Bottleneck Block</h3>
          <p class="usage">用于 ResNet-50 / ResNet-101 / ResNet-152</p>
          <div class="structure">
            <div class="layer">Conv 1×1</div>
            <div class="arrow">→</div>
            <div class="layer">BN → ReLU</div>
            <div class="arrow">→</div>
            <div class="layer">Conv 3×3</div>
            <div class="arrow">→</div>
            <div class="layer">BN → ReLU</div>
            <div class="arrow">→</div>
            <div class="layer">Conv 1×1</div>
            <div class="arrow">→</div>
            <div class="layer">BN</div>
          </div>
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
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 8px;
}

.usage {
  font-size: 14px;
  color: var(--text-muted);
  margin-bottom: 20px;
}

.structure {
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
  font-size: 16px;
}
</style>