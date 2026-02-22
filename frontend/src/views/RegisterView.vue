<template>
  <div class="auth-page">
    <form class="auth-form" @submit.prevent="submit">
      <h2>Create account</h2>
      <p v-if="error" class="form-error">{{ error }}</p>
      <label>
        Email
        <input v-model="email" type="email" required autocomplete="email" />
      </label>
      <label>
        Username
        <input v-model="username" type="text" required autocomplete="username" />
      </label>
      <label>
        Password
        <input v-model="password" type="password" required autocomplete="new-password" minlength="8" />
      </label>
      <button type="submit" :disabled="loading" class="btn btn-primary">
        {{ loading ? 'Creating account…' : 'Create account' }}
      </button>
      <p class="auth-switch">Already have an account? <RouterLink to="/login">Sign in</RouterLink></p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()

const email = ref('')
const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')

async function submit() {
  loading.value = true
  error.value = ''
  try {
    await auth.register(email.value, username.value, password.value)
    router.push('/dashboard')
  } catch (e) {
    const data = e.response?.data
    error.value = data
      ? Object.values(data).flat().join(' ')
      : 'Registration failed.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
@import './LoginView.vue';
</style>
