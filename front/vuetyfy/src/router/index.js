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
    path: '/Mypage',
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
    component: () => import('@/components/bottompushview/Reserve.vue'),
    children: [
      {
      path: '',
      name:'Reserve_list',
      component: () => import('@/components/bottompushview/Reserve_list.vue')
      },
      {
        path: '/Add', 
        name:'Add',
        component: () => import('@/components/bottompushview/Reserve_add_parents.vue'),
        children:[
          {
            path: '', 
            name:'Adding',
            component: () => import('@/components/bottompushview/Reserved_adding.vue'),

          },
          {
            path: '/Checking', 
            name:'Checking',
            component: () => import('@/components/bottompushview/Reserve_checking.vue')
          }
        ]
      },
        
    ]

  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
