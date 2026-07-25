# PPT HTML 开发指南

## 目录结构

```
public/workspaces/
├── index.json                    # 工作空间索引
├── deep-learning/                # 工作空间
│   ├── workspace.json           # 工作空间配置
│   ├── pooling/                 # PPT目录
│   │   └── presentation.html    # PPT文件
│   ├── activation/
│   │   └── presentation.html
│   └── resnet/
│       └── presentation.html
└── another-workspace/
    └── ...
```

## 快速创建新PPT

```bash
python create_ppt.py <workspace> <ppt-id> "<标题>"
```

示例：
```bash
python create_ppt.py deep-learning transformers "Transformer架构"
python create_ppt.py computer-vision yolo "YOLO目标检测"
```

## HTML模板结构

### 基本结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>标题</title>
  <style>
    /* CSS样式 */
  </style>
</head>
<body>
  <div class="presentation">
    <div class="slide slide-title active" data-index="0">...</div>
    <div class="slide slide-content" data-index="1">...</div>
    ...
  </div>
  <div class="nav-bar">...</div>
  <script>
    /* 导航逻辑 */
  </script>
</body>
</html>
```

### 可用的Slide类型

#### 1. 标题页 (slide-title)
```html
<div class="slide slide-title active" data-index="0">
  <div class="tag">分类标签</div>
  <h1>主标题</h1>
  <p class="subtitle">副标题</p>
  <div class="hint">按 → 切换页面</div>
</div>
```

#### 2. 内容页 (slide-content)
```html
<div class="slide slide-content" data-index="1">
  <div class="section-tag">01 / 章节</div>
  <h2>页面标题</h2>
  <div class="card-grid">
    <div class="card">
      <h3>要点</h3>
      <p>描述</p>
    </div>
  </div>
</div>
```

#### 3. 公式页
```html
<div class="slide slide-content" data-index="2">
  <div class="section-tag">02 / 公式</div>
  <h2>公式标题</h2>
  <div class="formula-box">
    <div class="formula-main">f(x) = ...</div>
    <div class="formula-note">说明</div>
  </div>
</div>
```

#### 4. 总结页 (slide-summary)
```html
<div class="slide slide-summary" data-index="3">
  <div class="section-tag">总结</div>
  <h2>核心要点</h2>
  <div class="summary-grid">
    <div class="summary-item">
      <div class="summary-icon">1</div>
      <div>
        <h3>要点</h3>
        <p>描述</p>
      </div>
    </div>
  </div>
</div>
```

## CSS变量

```css
:root {
  --bg: #0a0a0f;           /* 背景色 */
  --surface: #12121a;      /* 卡片背景 */
  --surface-2: #1a1a26;    /* 次级背景 */
  --accent: #00e5ff;       /* 主强调色 */
  --accent-2: #7c4dff;     /* 次强调色 */
  --accent-3: #ff6d00;     /* 第三强调色 */
  --text-primary: #eef0f6; /* 主文字色 */
  --text-muted: #6b6d7b;   /* 次文字色 */
  --green: #00e676;        /* 绿色 */
  --grid-cell: #1e1e2e;    /* 网格单元格 */
  --grid-border: #2a2a3d;  /* 网格边框 */
  --highlight: #ffab00;    /* 高亮色 */
}
```

## 动画

### fadeUp动画
卡片默认带有fadeUp动画，激活时自动播放：

```css
.card {
  opacity: 0;
  transform: translateY(20px);
}

.slide.active .card {
  animation: fadeUp 0.5s ease forwards;
}

.slide.active .card:nth-child(2) { animation-delay: 0.1s; }
.slide.active .card:nth-child(3) { animation-delay: 0.2s; }
.slide.active .card:nth-child(4) { animation-delay: 0.3s; }
```

## 工作空间配置

### index.json
```json
[
  {
    "id": "deep-learning",
    "name": "Deep Learning",
    "description": "深度学习",
    "presentations": [
      {
        "id": "pooling",
        "title": "池化",
        "description": "池化技术详解",
        "file": "presentation.html",
        "totalSlides": 8
      }
    ]
  }
]
```

### workspace.json
```json
{
  "id": "deep-learning",
  "name": "Deep Learning",
  "description": "深度学习",
  "presentations": [...]
}
```

## 最佳实践

1. **保持一致性**：使用统一的配色和样式
2. **动画适度**：不要过度使用动画，保持专业
3. **内容精简**：每页聚焦一个要点
4. **响应式设计**：确保在不同尺寸下正常显示
5. **字体选择**：使用系统字体，避免外部依赖

## 添加新工作空间

1. 在 `public/workspaces/` 下创建新目录
2. 运行 `create_ppt.py` 创建PPT
3. 系统会自动更新 `index.json`

## 调试技巧

1. 直接在浏览器中打开 `presentation.html` 测试
2. 使用开发者工具检查样式
3. 确保 `data-index` 从0开始连续编号
4. 第一个slide必须有 `active` 类