<template>
  <div class="auth-page">
    <form class="auth-form" @submit.prevent="submit">
      <h2>Sign in</h2>
      <p v-if="error" class="form-error">{{ error }}</p>
      <label>
        Email
        <input v-model="email" type="email" required autocomplete="email" />
      </label>
      <label>
        Password
        <input v-model="password" type="password" required autocomplete="current-password" />
      </label>
      <button type="submit" :disabled="loading" class="btn btn-primary">
        {{ loading ? 'Signing in…' : 'Sign in' }}
      </button>
      <p class="auth-switch">No account? <RouterLink to="/register">Register</RouterLink></p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute, RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()

const email = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')

async function submit() {
  loading.value = true
  error.value = ''
  try {
    await auth.login(email.value, password.value)
    router.push(route.query.redirect || '/dashboard')
  } catch (e) {
    error.value = e.response?.data?.non_field_errors?.[0] ?? 'Login failed.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 2rem;
}

.auth-form {
  background: #fff;
  border-radius: 14px;
  padding: 2.5rem;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 2px 16px rgba(0,0,0,.08);
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

h2 { font-size: 1.6rem; }

label {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  font-size: 0.9rem;
  font-weight: 500;
}

input {
  padding: 0.65rem 0.9rem;
  border: 1.5px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.15s;
}

input:focus { border-color: #1a1a1a; }

.btn { width: 100%; padding: 0.75rem; border: none; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; }
.btn-primary { background: #1a1a1a; color: #fff; }
.btn:disabled { opacity: 0.6; cursor: not-allowed; }

.form-error { color: #c0392b; font-size: 0.9rem; }
.auth-switch { text-align: center; font-size: 0.9rem; }
.auth-switch a { font-weight: 600; text-decoration: underline; }
</style>
