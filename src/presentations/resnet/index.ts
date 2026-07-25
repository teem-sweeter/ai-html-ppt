import type { Presentation } from '../registry'

export const resnetPresentation: Presentation = {
  id: 'resnet',
  title: 'ResNet',
  description: '残差网络详解',
  slides: [
    () => import('./Slide0.vue'),
    () => import('./Slide1.vue'),
    () => import('./Slide2.vue'),
    () => import('./Slide3.vue'),
    () => import('./Slide4.vue'),
    () => import('./Slide5.vue'),
    () => import('./Slide6.vue'),
    () => import('./Slide7.vue'),
    () => import('./Slide8.vue'),
    () => import('./Slide9.vue'),
  ]
}