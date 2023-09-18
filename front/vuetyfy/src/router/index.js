// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '',
    component: () => import('@/views/Home.vue'),

    children: [
      {
        path: '/Sample',
        name:'Sample',
        component: () => import('@/components/samp.vue'),
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
