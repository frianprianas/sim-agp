import { defineStore } from 'pinia'
import { authService } from '@/services'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: authService.getCurrentUser(),
    token: localStorage.getItem('token'),
    isAuthenticated: authService.isAuthenticated(),
  }),

  getters: {
    isAdmin: (state) => state.user?.role === 'admin',
    isMahasiswa: (state) => state.user?.role === 'mahasiswa',
  },

  actions: {
    async login(username, password) {
      try {
        const data = await authService.login(username, password)
        this.user = data.user
        this.token = data.token
        this.isAuthenticated = true
        return data
      } catch (error) {
        throw error
      }
    },

    async register(userData) {
      try {
        const data = await authService.register(userData)
        this.user = data.user
        this.token = data.token
        this.isAuthenticated = true
        return data
      } catch (error) {
        throw error
      }
    },

    async logout() {
      try {
        await authService.logout()
      } finally {
        this.user = null
        this.token = null
        this.isAuthenticated = false
      }
    },

    async fetchProfile() {
      try {
        const user = await authService.getProfile()
        this.user = user
        localStorage.setItem('user', JSON.stringify(user))
      } catch (error) {
        throw error
      }
    },
  },
})
