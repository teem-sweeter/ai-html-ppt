// 幻灯片配置
export interface SlideConfig {
  file: string        // 文件名（支持 html, md, pptx）
  title?: string      // 幻灯片标题
}

// PPT 配置
export interface PresentationConfig {
  id: string
  title: string
  description: string
  slides: SlideConfig[]
}

// 工作空间配置
export interface Workspace {
  id: string
  name: string
  description: string
  presentations: PresentationConfig[]
}

// 运行时 PPT 对象（包含加载函数）
export interface Presentation {
  id: string
  title: string
  description: string
  workspace: string
  slides: Array<() => Promise<any>>
}

// 自动发现所有工作空间
const workspaceModules = import.meta.glob<{ [key: string]: Workspace }>('./**/index.ts', { eager: true })

// 工作空间列表
export const WORKSPACES: Workspace[] = []

// 所有 PPT 列表
export const PRESENTATIONS: Presentation[] = []

// 加载工作空间配置
for (const path in workspaceModules) {
  const module = workspaceModules[path]
  const keys = Object.keys(module)
  if (keys.length > 0) {
    const workspace = module[keys[0]]
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
            const filePath = `./${workspace.id}/${presConfig.id}/${slide.file}`
            
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
    const html = await response.text()
    
    // 创建一个 Vue 组件来渲染 HTML
    return {
      default: {
        template: `<div class="html-slide" v-html="content"></div>`,
        setup() {
          return { content: html }
        }
      }
    }
  } catch (error) {
    console.error(`Failed to load HTML slide: ${path}`, error)
    // 返回一个错误占位组件
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

// Markdown 文件加载器
async function loadMarkdownSlide(path: string): Promise<any> {
  try {
    const response = await fetch(path)
    const md = await response.text()
    
    // 简单的 Markdown 转 HTML（实际项目中可以使用 marked 或 markdown-it）
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