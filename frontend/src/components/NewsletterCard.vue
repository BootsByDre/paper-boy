<template>
  <div class="card">
    <div class="card-header">
      <RouterLink :to="`/newsletters/${newsletter.id}`" class="card-title">
        {{ newsletter.name }}
      </RouterLink>
      <span class="badge" :class="newsletter.is_active ? 'active' : 'inactive'">
        {{ newsletter.is_active ? 'Active' : 'Paused' }}
      </span>
    </div>
    <p class="topic">{{ truncate(newsletter.topic, 100) }}</p>
    <div class="card-footer">
      <span class="cadence capitalize">{{ newsletter.cadence }}</span>
      <button class="btn-delete" @click="$emit('delete')">Delete</button>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({ newsletter: Object })
defineEmits(['delete'])

function truncate(str, n) {
  return str.length > n ? str.slice(0, n) + '…' : str
}
</script>

<style scoped>
.card {
  background: #fff;
  border-radius: 12px;
  padding: 1.25rem 1.5rem;
  box-shadow: 0 1px 4px rgba(0,0,0,.06);
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
}

.card-title {
  font-weight: 600;
  font-size: 1rem;
}

.card-title:hover { text-decoration: underline; }

.badge { display: inline-block; padding: 0.15rem 0.55rem; border-radius: 99px; font-size: 0.75rem; font-weight: 600; }
.badge.active { background: #d4f7d4; color: #1a6b1a; }
.badge.inactive { background: #f0f0f0; color: #666; }

.topic { font-size: 0.875rem; color: #666; line-height: 1.5; }

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
}

.cadence { font-size: 0.8rem; color: #888; }
.capitalize { text-transform: capitalize; }

.btn-delete {
  background: none;
  border: none;
  font-size: 0.8rem;
  color: #c0392b;
  cursor: pointer;
  font-weight: 500;
}

.btn-delete:hover { text-decoration: underline; }
</style>
