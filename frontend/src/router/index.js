import { createRouter, createWebHistory } from 'vue-router'
import { authService } from '@/services'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      redirect: '/dashboard',
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/views/Login.vue'),
      meta: { requiresGuest: true },
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import('@/views/Register.vue'),
      meta: { requiresGuest: true },
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: () => import('@/views/Dashboard.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/mahasiswa',
      name: 'MahasiswaList',
      component: () => import('@/views/mahasiswa/List.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/mahasiswa/create',
      name: 'MahasiswaCreate',
      component: () => import('@/views/mahasiswa/Form.vue'),
      meta: { requiresAuth: true, requiresAdmin: true },
    },
    {
      path: '/mahasiswa/:nim/edit',
      name: 'MahasiswaEdit',
      component: () => import('@/views/mahasiswa/Form.vue'),
      meta: { requiresAuth: true, requiresAdmin: true },
    },
    {
      path: '/mahasiswa/:nim',
      name: 'MahasiswaDetail',
      component: () => import('@/views/mahasiswa/Detail.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/prodi',
      name: 'ProdiList',
      component: () => import('@/views/prodi/Index.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/prodi/create',
      name: 'ProdiCreate',
      component: () => import('@/views/prodi/Form.vue'),
      meta: { requiresAuth: true, requiresAdmin: true },
    },
    {
      path: '/prodi/edit/:id',
      name: 'ProdiEdit',
      component: () => import('@/views/prodi/Form.vue'),
      meta: { requiresAuth: true, requiresAdmin: true },
    },
    {
      path: '/profile',
      name: 'Profile',
      component: () => import('@/views/Profile.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/settings',
      name: 'Settings',
      component: () => import('@/views/Settings.vue'),
      meta: { requiresAuth: true },
    },
  ],
})

// Navigation guards
router.beforeEach((to, from, next) => {
  const isAuthenticated = authService.isAuthenticated()
  const user = authService.getCurrentUser()

  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login')
  } else if (to.meta.requiresGuest && isAuthenticated) {
    next('/dashboard')
  } else if (to.meta.requiresAdmin && user?.role !== 'admin') {
    next('/dashboard')
  } else {
    next()
  }
})

export default router
