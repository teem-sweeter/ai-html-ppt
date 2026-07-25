import type { Workspace } from '../registry'

export const deepLearningWorkspace: Workspace = {
  id: 'deep-learning',
  name: '深度学习',
  description: '深度学习基础知识',
  presentations: [
    {
      id: 'pooling',
      title: '池化',
      description: '池化技术详解 - 用更少的信息量保留最重要的内容',
      slides: [
        { file: 'slide0.html', title: '标题页' },
        { file: 'slide1.html', title: '核心概念' },
        { file: 'slide2.html', title: 'Step 1' },
        { file: 'slide3.html', title: 'Step 2' },
        { file: 'slide4.html', title: 'Step 3' },
        { file: 'slide5.html', title: 'Step 4' },
        { file: 'slide6.html', title: '最终结果' },
        { file: 'slide7.html', title: '总结' },
      ]
    },
    {
      id: 'activation',
      title: '激活函数',
      description: '激活函数详解 - 赋予神经网络非线性力量的核心机制',
      slides: [
        { file: 'slide0.html', title: '标题页' },
        { file: 'slide1.html', title: '核心概念' },
        { file: 'slide2.html', title: 'Sigmoid' },
        { file: 'slide3.html', title: 'Tanh' },
        { file: 'slide4.html', title: 'ReLU' },
        { file: 'slide5.html', title: 'ReLU变体' },
        { file: 'slide6.html', title: 'GELU & Swish' },
        { file: 'slide7.html', title: '对比' },
        { file: 'slide8.html', title: '实践指南' },
        { file: 'slide9.html', title: '总结' },
      ]
    },
    {
      id: 'resnet',
      title: 'ResNet',
      description: '残差网络详解 - 让神经网络突破千层的关键创新',
      slides: [
        { file: 'slide0.html', title: '标题页' },
        { file: 'slide1.html', title: '问题背景' },
        { file: 'slide2.html', title: '核心思想' },
        { file: 'slide3.html', title: '残差块结构' },
        { file: 'slide4.html', title: '数学表达' },
        { file: 'slide5.html', title: '两种残差块' },
        { file: 'slide6.html', title: '网络架构' },
        { file: 'slide7.html', title: '为什么有效' },
        { file: 'slide8.html', title: '实验结果' },
        { file: 'slide9.html', title: '总结' },
      ]
    }
  ]
}