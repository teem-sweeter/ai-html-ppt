# AI HTML PPT

基于 Vue 3 + Vite + TypeScript 的 AI HTML PPT 演示系统，支持自动发现、动态加载、全屏展示等功能。

## ✨ 功能特点

- 🎯 **自动发现** - 无需手动注册，自动扫描并加载 PPT 演示文稿
- 📱 **响应式设计** - 支持桌面端和移动端，自适应屏幕尺寸
- 🖥️ **全屏展示** - 支持全屏播放，提供沉浸式演示体验
- ⌨️ **多种翻页方式** - 键盘方向键、鼠标点击、触摸滑动、导航按钮
- 🎨 **精美动画** - 流畅的过渡动画和交互效果
- 📦 **按需加载** - 每页独立加载，优化首屏加载速度
- 🔧 **易于扩展** - 简单的目录结构，轻松添加新的 PPT

## 🚀 快速开始

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
npm run dev
```

访问 http://localhost:5173 查看效果。

### 构建生产版本

```bash
npm run build
```

构建产物将输出到 `dist` 目录。

### 预览生产版本

```bash
npm run preview
```

## 📁 项目结构

```
ppt-viewer/
├── public/                    # 静态资源
├── src/
│   ├── assets/               # 全局样式、字体等
│   │   └── base.css          # 基础样式和 CSS 变量
│   ├── components/           # 核心组件
│   │   ├── Sidebar.vue       # 左侧 PPT 列表组件
│   │   ├── Player.vue        # 右侧 PPT 播放器核心组件
│   │   └── ProgressBar.vue   # 底部进度条和导航组件
│   ├── presentations/        # 🌟 PPT 内容存放区
│   │   ├── registry.ts       # 全局 PPT 注册中心（自动发现）
│   │   ├── pooling/          # 池化 PPT 示例
│   │   ├── activation/       # 激活函数 PPT 示例
│   │   └── resnet/           # ResNet PPT 示例
│   ├── App.vue               # 主布局
│   └── main.ts               # 入口文件
├── index.html                # HTML 入口
├── vite.config.ts            # Vite 配置
├── tsconfig.json             # TypeScript 配置
└── package.json              # 项目配置
```

## 📝 如何添加新的 PPT

### 1. 创建 PPT 目录

在 `src/presentations/` 下创建新目录：

```bash
mkdir src/presentations/my-ppt
```

### 2. 创建配置文件

在新目录下创建 `index.ts` 文件：

```typescript
import type { Presentation } from '../registry'

export const myPptPresentation: Presentation = {
  id: 'my-ppt',                    // 唯一标识符
  title: '我的 PPT',               // 显示标题
  description: 'PPT 描述信息',     // 描述信息
  slides: [
    () => import('./Slide0.vue'),  // 第 0 页
    () => import('./Slide1.vue'),  // 第 1 页
    () => import('./Slide2.vue'),  // 第 2 页
    // ... 添加更多页
  ]
}
```

### 3. 创建 Slide 组件

创建对应的 Vue 组件文件：

```vue
<!-- Slide0.vue -->
<template>
  <div class="slide">
    <h1>我的 PPT 标题</h1>
    <p>副标题或描述</p>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.slide {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  text-align: center;
}

h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  color: var(--accent);
}
</style>
```

### 4. 重启开发服务器

```bash
npm run dev
```

新的 PPT 将自动出现在左侧边栏中。

## 🎮 使用说明

### 翻页操作

| 操作 | 方式 |
|------|------|
| 下一页 | `→` 键、`↓` 键、空格键、点击右侧区域、左滑 |
| 上一页 | `←` 键、`↑` 键、点击左侧区域、右滑 |
| 跳转页面 | 点击底部导航点 |
| 全屏 | 点击右上角全屏按钮 |

### 全屏模式

- 点击播放区域右上角的全屏按钮进入全屏模式
- 全屏模式下只显示播放区域，隐藏其他 UI 元素
- 按 `Esc` 键或点击全屏按钮退出全屏

## 🛠️ 技术栈

- **Vue 3** - 渐进式 JavaScript 框架
- **Vite** - 下一代前端构建工具
- **TypeScript** - JavaScript 的超集
- **CSS Variables** - 主题色彩管理
- **Dynamic Import** - 按需加载优化

## 📄 开源许可证

本项目基于 [MIT License](LICENSE) 开源。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 🔗 相关链接

- [GitHub 仓库](https://github.com/teem-sweeter/ai-html-ppt)
- [问题反馈](https://github.com/teem-sweeter/ai-html-ppt/issues)

---

如果这个项目对你有帮助，请给一个 ⭐️ Star 支持一下！