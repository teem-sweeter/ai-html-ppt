<template>
  <div class="slide slide-content">
    <div class="section-label">06 / 网络架构</div>
    <div class="big-text">ResNet 家族 <span class="highlight">全景</span></div>
    <div class="content">
      <div class="architecture">
        <div class="architecture-item">
          <div class="model-name">ResNet-18</div>
          <div class="model-detail">
            <div class="layers">18层</div>
            <div class="blocks">Basic Block</div>
            <div class="params">11.7M参数</div>
          </div>
        </div>
        <div class="architecture-item">
          <div class="model-name">ResNet-34</div>
          <div class="model-detail">
            <div class="layers">34层</div>
            <div class="blocks">Basic Block</div>
            <div class="params">21.8M参数</div>
          </div>
        </div>
        <div class="architecture-item">
          <div class="model-name">ResNet-50</div>
          <div class="model-detail">
            <div class="layers">50层</div>
            <div class="blocks">Bottleneck Block</div>
            <div class="params">25.6M参数</div>
          </div>
        </div>
        <div class="architecture-item">
          <div class="model-name">ResNet-101</div>
          <div class="model-detail">
            <div class="layers">101层</div>
            <div class="blocks">Bottleneck Block</div>
            <div class="params">44.5M参数</div>
          </div>
        </div>
        <div class="architecture-item">
          <div class="model-name">ResNet-152</div>
          <div class="model-detail">
            <div class="layers">152层</div>
            <div class="blocks">Bottleneck Block</div>
            <div class="params">60.2M参数</div>
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

.highlight {
  color: var(--accent);
}

.content {
  width: 100%;
  max-width: 1100px;
}

.architecture {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.architecture-item {
  flex: 1;
  min-width: 200px;
  background: var(--surface);
  border: 1px solid var(--grid-border);
  border-radius: 6px;
  padding: 20px;
}

.model-name {
  font-family: 'JetBrains Mono', monospace;
  font-size: 18px;
  font-weight: 700;
  color: var(--accent);
  margin-bottom: 12px;
}

.model-detail {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.layers, .blocks, .params {
  font-size: 14px;
  color: var(--text-muted);
}

.layers::before {
  content: '层数: ';
  color: var(--text-primary);
  font-weight: 700;
}

.blocks::before {
  content: '块类型: ';
  color: var(--text-primary);
  font-weight: 700;
}

.params::before {
  content: '参数量: ';
  color: var(--text-primary);
  font-weight: 700;
}
</style>