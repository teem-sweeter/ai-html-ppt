// 从工作空间模块导入类型
export interface SlideConfig {
  file: string
  title?: string
}

export interface PresentationConfig {
  id: string
  title: string
  description: string
  slides: SlideConfig[]
}

export interface Workspace {
  id: string
  name: string
  description: string
  presentations: PresentationConfig[]
}

export interface Presentation {
  id: string
  title: string
  description: string
  workspace: string
  slides: Array<() => Promise<any>>
}

// 自动发现所有工作空间
// 使用相对于项目根目录的路径
const workspaceModules = import.meta.glob<{ [key: string]: Workspace }>('/workspaces/**/index.ts', { eager: true })

// 工作空间列表
export const WORKSPACES: Workspace[] = []

// 所有 PPT 列表
export const PRESENTATIONS: Presentation[] = []

console.log('Found workspace modules:', workspaceModules)

// 加载工作空间配置
for (const path in workspaceModules) {
  const module = workspaceModules[path]
  console.log('Processing module:', path, module)
  
  const keys = Object.keys(module)
  if (keys.length > 0) {
    const workspace = module[keys[0]]
    console.log('Workspace:', workspace)
    
    if (workspace && workspace.id && workspace.presentations) {
      WORKSPACES.push(workspace)
      
      // 为每个 PPT 创建加载函数
      for (const presConfig of workspace.presentations) {
        const presentation: Presentation = {
          id: presConfig.id,
          title: presConfig.title,
          description: presConfig.description,
          workspace: workspace.id,
          slides: presConfig.slides.map(slide => {
            // 根据文件扩展名创建不同的加载函数
            // 使用绝对路径，从根目录访问
            const filePath = `/workspaces/${workspace.id}/${presConfig.id}/${slide.file}`
            
            if (slide.file.endsWith('.html')) {
              return () => loadHtmlSlide(filePath)
            } else if (slide.file.endsWith('.md')) {
              return () => loadMarkdownSlide(filePath)
            } else {
              // 默认尝试加载为 Vue 组件
              return () => import(/* @vite-ignore */ filePath)
            }
          })
        }
        PRESENTATIONS.push(presentation)
      }
    }
  }
}

console.log('Loaded presentations:', PRESENTATIONS)

// 按工作空间和 id 排序
WORKSPACES.sort((a, b) => a.id.localeCompare(b.id))
PRESENTATIONS.sort((a, b) => {
  if (a.workspace !== b.workspace) {
    return a.workspace.localeCompare(b.workspace)
  }
  return a.id.localeCompare(b.id)
})

// HTML 文件加载器
async function loadHtmlSlide(path: string): Promise<any> {
  try {
    const response = await fetch(path)
    let html = await response.text()
    
    // 移除 Vite 注入的 script 标签
    html = html.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
    
    // 创建一个 Vue 组件来渲染 HTML
    // 直接返回组件选项对象，而不是包含 default 的模块
    return {
      template: `<div class="html-slide-wrapper" v-html="content"></div>`,
      setup() {
        return { content: html }
      }
    }
  } catch (error) {
    console.error(`Failed to load HTML slide: ${path}`, error)
    // 返回一个错误占位组件
    return {
      template: `<div class="slide-error">加载失败: {{ path }}</div>`,
      setup() {
        return { path }
      }
    }
  }
}

// Markdown 文件加载器
async function loadMarkdownSlide(path: string): Promise<any> {
  try {
    const response = await fetch(path)
    const md = await response.text()
    
    // 简单的 Markdown 转 HTML
    const html = simpleMarkdownToHtml(md)
    
    return {
      default: {
        template: `<div class="markdown-slide" v-html="content"></div>`,
        setup() {
          return { content: html }
        }
      }
    }
  } catch (error) {
    console.error(`Failed to load Markdown slide: ${path}`, error)
    return {
      default: {
        template: `<div class="slide-error">加载失败: {{ path }}</div>`,
        setup() {
          return { path }
        }
      }
    }
  }
}

// 简单的 Markdown 转 HTML 函数
function simpleMarkdownToHtml(md: string): string {
  let html = md
    // 标题
    .replace(/^### (.*$)/gm, '<h3>$1</h3>')
    .replace(/^## (.*$)/gm, '<h2>$1</h2>')
    .replace(/^# (.*$)/gm, '<h1>$1</h1>')
    // 粗体和斜体
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    // 链接
    .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2">$1</a>')
    // 换行
    .replace(/\n\n/g, '</p><p>')
    .replace(/\n/g, '<br>')
  
  // 包装在段落中
  if (!html.startsWith('<h')) {
    html = '<p>' + html + '</p>'
  }
  
  return html
}