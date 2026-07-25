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

const workspaceModules = import.meta.glob<{ [key: string]: Workspace }>('../../workspaces/**/index.ts', { eager: true })

export const WORKSPACES: Workspace[] = []
export const PRESENTATIONS: Presentation[] = []

for (const path in workspaceModules) {
  const module = workspaceModules[path]
  const keys = Object.keys(module)
  if (keys.length > 0) {
    const workspace = module[keys[0]]
    if (workspace && workspace.id && workspace.presentations) {
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
  }
}

WORKSPACES.sort((a, b) => a.id.localeCompare(b.id))
PRESENTATIONS.sort((a, b) => {
  if (a.workspace !== b.workspace) return a.workspace.localeCompare(b.workspace)
  return a.id.localeCompare(b.id)
})