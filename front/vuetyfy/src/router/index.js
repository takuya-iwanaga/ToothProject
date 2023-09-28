// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/views/Home.vue'),

  
    children: [
      
    ],
  },
  {
    path: '/Medical',
    name:'Medical',
    component: () => import('@/components/bottompushview/MedicalBox.vue')
  },
  {
    path: '/Information',
    name:'Information',
    component: () => import('@/components/bottompushview/Information.vue')
  },
  {
    path: '/Mypage/:name',
    name:'Mypage',
    component: () => import('@/components/bottompushview/Mypage.vue'),
  },
  {
    path: '/Qrcode',
    name:'Qrcode',
    component: () => import('@/components/bottompushview/Qrcode.vue')
  },
  {
    path: '/Reserve',
    name:'Reserve',
    component: () => import('@/components/bottompushview/Reserve.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
