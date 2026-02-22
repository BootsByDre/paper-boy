<template>
  <div id="app">
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<style>
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Inter, system-ui, -apple-system, sans-serif;
  background: #f8f7f4;
  color: #1a1a1a;
  line-height: 1.6;
}

a {
  color: inherit;
  text-decoration: none;
}
</style>
