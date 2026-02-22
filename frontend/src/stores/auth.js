import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { auth as authApi } from '@/api/auth'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token') || null)
  const user = ref(null)

  const isLoggedIn = computed(() => !!token.value)

  async function login(email, password) {
    const { data } = await authApi.login({ email, password })
    token.value = data.key
    user.value = data.user
    localStorage.setItem('token', data.key)
  }

  async function register(email, username, password) {
    const { data } = await authApi.register({ email, username, password })
    token.value = data.key
    user.value = data.user
    localStorage.setItem('token', data.key)
  }

  async function fetchMe() {
    if (!token.value) return
    const { data } = await authApi.me()
    user.value = data
  }

  async function logout() {
    await authApi.logout()
    token.value = null
    user.value = null
    localStorage.removeItem('token')
  }

  return { token, user, isLoggedIn, login, register, fetchMe, logout }
})
