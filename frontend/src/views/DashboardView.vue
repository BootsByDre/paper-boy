<template>
  <div class="layout">
    <AppNav />
    <main class="dashboard">
      <div class="dashboard-header">
        <h1>My Newsletters</h1>
        <RouterLink to="/newsletters/new" class="btn btn-primary">+ New newsletter</RouterLink>
      </div>

      <div v-if="store.loading" class="status">Loading…</div>
      <div v-else-if="store.error" class="status error">{{ store.error }}</div>
      <div v-else-if="store.items.length === 0" class="empty">
        <p>You don't have any newsletters yet.</p>
        <RouterLink to="/newsletters/new">Create your first one</RouterLink>
      </div>
      <div v-else class="newsletter-grid">
        <NewsletterCard
          v-for="n in store.items"
          :key="n.id"
          :newsletter="n"
          @delete="handleDelete(n.id)"
        />
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useNewslettersStore } from '@/stores/newsletters'
import AppNav from '@/components/AppNav.vue'
import NewsletterCard from '@/components/NewsletterCard.vue'

const store = useNewslettersStore()

onMounted(() => store.fetchAll())

async function handleDelete(id) {
  if (!confirm('Delete this newsletter?')) return
  await store.remove(id)
}
</script>

<style scoped>
.layout { min-height: 100vh; display: flex; flex-direction: column; }
.dashboard { max-width: 900px; margin: 0 auto; padding: 2rem 1.5rem; width: 100%; }
.dashboard-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; }
h1 { font-size: 1.8rem; }
.btn { padding: 0.65rem 1.25rem; border: none; border-radius: 8px; font-size: 0.95rem; font-weight: 600; cursor: pointer; }
.btn-primary { background: #1a1a1a; color: #fff; }
.newsletter-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.25rem; }
.status { text-align: center; padding: 3rem; color: #777; }
.status.error { color: #c0392b; }
.empty { text-align: center; padding: 4rem; color: #555; }
.empty a { font-weight: 600; text-decoration: underline; }
</style>
