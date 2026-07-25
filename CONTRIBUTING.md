# 贡献指南

感谢你对 AI HTML PPT 项目的关注！我们欢迎任何形式的贡献。

## 如何贡献

### 报告 Bug

如果你发现了 Bug，请通过 [GitHub Issues](https://github.com/teem-sweeter/ai-html-ppt/issues) 提交，并包含以下信息：

1. Bug 的详细描述
2. 复现步骤
3. 期望的行为
4. 实际的行为
5. 运行环境（操作系统、Node.js 版本、浏览器版本等）

### 功能建议

如果你有新功能的建议，也欢迎通过 Issue 提交。请详细描述：

1. 功能的使用场景
2. 期望的实现方式
3. 可能的替代方案

### 提交代码

1. Fork 本仓库
2. 创建你的特性分支：
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. 提交你的更改：
   ```bash
   git commit -m 'feat: add some AmazingFeature'
   ```
4. 推送到分支：
   ```bash
   git push origin feature/AmazingFeature
   ```
5. 打开一个 Pull Request

### Commit 规范

请使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat:` 新功能
- `fix:` 修复 Bug
- `docs:` 文档更新
- `style:` 代码格式（不影响代码运行的变动）
- `refactor:` 重构（既不是新增功能，也不是修改 bug 的代码变动）
- `perf:` 性能优化
- `test:` 增加测试
- `chore:` 构建过程或辅助工具的变动

### 代码风格

- 使用 TypeScript 编写代码
- 遵循 Vue 3 Composition API 的最佳实践
- 使用 `<script setup>` 语法
- 保持代码简洁，添加必要的注释

## 开发环境

1. 克隆仓库：
   ```bash
   git clone https://github.com/teem-sweeter/ai-html-ppt.git
   cd ai-html-ppt
   ```

2. 安装依赖：
   ```bash
   npm install
   ```

3. 启动开发服务器：
   ```bash
   npm run dev
   ```

4. 访问 http://localhost:5173 查看效果

## 添加新的 PPT

参考 [README.md](README.md) 中的"如何添加新的 PPT"部分。

## 许可证

提交代码即表示你同意你的代码将在 [MIT License](LICENSE) 下发布。