import type { Presentation } from '../registry'

export const poolingPresentation: Presentation = {
  id: 'pooling',
  title: '池化PPT',
  description: '池化技术详解',
  slides: [
    () => import('./Slide0.vue'),
    () => import('./Slide1.vue'),
    () => import('./Slide2.vue'),
    () => import('./Slide3.vue'),
    () => import('./Slide4.vue'),
    () => import('./Slide5.vue'),
    () => import('./Slide6.vue'),
    () => import('./Slide7.vue'),
  ]
}