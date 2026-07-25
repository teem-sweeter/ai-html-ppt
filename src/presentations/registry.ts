export interface PresentationConfig {
  id: string
  title: string
  description: string
  file: string
  totalSlides: number
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
  file: string
  totalSlides: number
}

export const WORKSPACES: Workspace[] = []
export const PRESENTATIONS: Presentation[] = []

// 从 public/workspaces/index.json 加载工作空间配置
async function loadWorkspaces() {
  try {
    const response = await fetch('/workspaces/index.json')
    const workspaces: Workspace[] = await response.json()

    for (const workspace of workspaces) {
      WORKSPACES.push(workspace)
      for (const presConfig of workspace.presentations) {
        PRESENTATIONS.push({
          id: presConfig.id,
          title: presConfig.title,
          description: presConfig.description,
          workspace: workspace.id,
          file: presConfig.file,
          totalSlides: presConfig.totalSlides
        })
      }
    }

    WORKSPACES.sort((a, b) => a.id.localeCompare(b.id))
    PRESENTATIONS.sort((a, b) => {
      if (a.workspace !== b.workspace) return a.workspace.localeCompare(b.workspace)
      return a.id.localeCompare(b.id)
    })
  } catch (e) {
    console.error('Failed to load workspaces:', e)
  }
}

// 导出加载完成的 Promise
export const workspacesReady = loadWorkspaces()