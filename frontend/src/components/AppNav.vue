<template>
  <nav class="nav">
    <RouterLink to="/dashboard" class="nav-brand">Paper Boy</RouterLink>
    <div class="nav-right">
      <span class="nav-user">{{ auth.user?.email }}</span>
      <button class="btn-logout" @click="handleLogout">Sign out</button>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()

async function handleLogout() {
  await auth.logout()
  router.push('/')
}
</script>

<style scoped>
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1.5rem;
  height: 56px;
  background: #fff;
  border-bottom: 1px solid #eee;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-brand {
  font-weight: 700;
  font-size: 1.1rem;
  letter-spacing: -0.02em;
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav-user {
  font-size: 0.875rem;
  color: #666;
}

.btn-logout {
  background: none;
  border: none;
  font-size: 0.875rem;
  cursor: pointer;
  color: #1a1a1a;
  font-weight: 500;
  text-decoration: underline;
}
</style>
