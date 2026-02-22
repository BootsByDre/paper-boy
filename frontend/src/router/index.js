import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const routes = [
  {
    path: '/',
    component: () => import('@/views/HomeView.vue'),
    meta: { requiresAuth: false },
  },
  {
    path: '/login',
    component: () => import('@/views/LoginView.vue'),
    meta: { requiresAuth: false },
  },
  {
    path: '/register',
    component: () => import('@/views/RegisterView.vue'),
    meta: { requiresAuth: false },
  },
  {
    path: '/dashboard',
    component: () => import('@/views/DashboardView.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: '/newsletters/new',
    component: () => import('@/views/NewsletterFormView.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: '/newsletters/:id',
    component: () => import('@/views/NewsletterDetailView.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: '/newsletters/:id/edit',
    component: () => import('@/views/NewsletterFormView.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: '/:pathMatch(.*)*',
    component: () => import('@/views/NotFoundView.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to) => {
  const auth = useAuthStore()
  if (to.meta.requiresAuth && !auth.isLoggedIn) {
    return { path: '/login', query: { redirect: to.fullPath } }
  }
  if ((to.path === '/login' || to.path === '/register') && auth.isLoggedIn) {
    return { path: '/dashboard' }
  }
})

export default router
