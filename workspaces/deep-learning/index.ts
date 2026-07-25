import type { Workspace } from '../registry'

export const deepLearningWorkspace: Workspace = {
  id: 'deep-learning',
  name: '深度学习',
  description: '深度学习基础知识',
  presentations: [
    {
      id: 'pooling',
      title: '池化',
      description: '池化技术详解',
      file: 'presentation.html',
      totalSlides: 8
    },
    {
      id: 'activation',
      title: '激活函数',
      description: '激活函数详解',
      file: 'presentation.html',
      totalSlides: 10
    },
    {
      id: 'resnet',
      title: 'ResNet',
      description: '残差网络详解',
      file: 'presentation.html',
      totalSlides: 10
    }
  ]
}