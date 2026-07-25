export interface SlideModule {
  default: () => Promise<any>
}

export interface Presentation {
  id: string
  title: string
  description: string
  slides: Array<() => Promise<any>>
}

// 自动发现 presentations 目录下的所有 PPT 配置
const presentationModules = import.meta.glob<{ [key: string]: Presentation }>('./**/index.ts', { eager: true })

// 提取并注册所有 PPT
export const PRESENTATIONS: Presentation[] = []

for (const path in presentationModules) {
  const module = presentationModules[path]
  // 获取导出的 Presentation 对象（通常是第一个导出）
  const keys = Object.keys(module)
  if (keys.length > 0) {
    const presentation = module[keys[0]]
    if (presentation && presentation.id && presentation.slides) {
      PRESENTATIONS.push(presentation)
    }
  }
}

// 按 id 排序，确保顺序稳定
PRESENTATIONS.sort((a, b) => a.id.localeCompare(b.id))