<template>
  <div class="not-found">
    <h1>404</h1>
    <p>Page not found.</p>
    <RouterLink to="/">Go home</RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.not-found {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  gap: 1rem;
  color: #555;
}
h1 { font-size: 5rem; color: #1a1a1a; }
a { font-weight: 600; text-decoration: underline; }
</style>
