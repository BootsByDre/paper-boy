<template>
  <div class="layout">
    <AppNav />
    <main class="detail-page" v-if="store.current">
      <div class="detail-header">
        <div>
          <h1>{{ store.current.name }}</h1>
          <span class="badge" :class="store.current.is_active ? 'active' : 'inactive'">
            {{ store.current.is_active ? 'Active' : 'Paused' }}
          </span>
        </div>
        <div class="detail-actions">
          <button class="btn btn-ghost" :disabled="triggering" @click="triggerNow">
            {{ triggering ? 'Sending…' : 'Send now' }}
          </button>
          <RouterLink :to="`/newsletters/${store.current.id}/edit`" class="btn btn-primary">
            Edit
          </RouterLink>
        </div>
      </div>

      <dl class="meta">
        <dt>Topic</dt><dd>{{ store.current.topic }}</dd>
        <dt>Cadence</dt><dd class="capitalize">{{ store.current.cadence }}</dd>
        <dt>Last delivered</dt>
        <dd>{{ store.current.last_delivered_at ? formatDate(store.current.last_delivered_at) : 'Never' }}</dd>
      </dl>

      <section class="digests">
        <h2>Past digests</h2>
        <p v-if="store.digests.length === 0" class="muted">No digests generated yet.</p>
        <div v-for="d in store.digests" :key="d.id" class="digest-row">
          <span class="digest-date">{{ formatDate(d.window_end) }}</span>
          <span class="digest-status" :class="d.status">{{ d.status }}</span>
        </div>
      </section>
    </main>
    <div v-else class="status">Loading…</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { useNewslettersStore } from '@/stores/newsletters'
import AppNav from '@/components/AppNav.vue'

const route = useRoute()
const store = useNewslettersStore()
const triggering = ref(false)

onMounted(async () => {
  await Promise.all([
    store.fetchOne(route.params.id),
    store.fetchDigests(route.params.id),
  ])
})

async function triggerNow() {
  triggering.value = true
  try {
    await store.trigger(route.params.id)
    alert('Digest generation started — check back shortly.')
  } finally {
    triggering.value = false
  }
}

function formatDate(iso) {
  return new Date(iso).toLocaleDateString('en-US', {
    year: 'numeric', month: 'short', day: 'numeric',
  })
}
</script>

<style scoped>
.layout { min-height: 100vh; display: flex; flex-direction: column; }
.detail-page { max-width: 700px; margin: 0 auto; padding: 2rem 1.5rem; width: 100%; }
.detail-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem; }
h1 { font-size: 1.8rem; margin-bottom: 0.4rem; }
.badge { display: inline-block; padding: 0.2rem 0.65rem; border-radius: 99px; font-size: 0.8rem; font-weight: 600; }
.badge.active { background: #d4f7d4; color: #1a6b1a; }
.badge.inactive { background: #f0f0f0; color: #666; }
.detail-actions { display: flex; gap: 0.75rem; }
.btn { padding: 0.6rem 1.2rem; border-radius: 8px; font-size: 0.9rem; font-weight: 600; cursor: pointer; border: none; }
.btn-primary { background: #1a1a1a; color: #fff; }
.btn-ghost { background: transparent; color: #1a1a1a; border: 2px solid #1a1a1a; }
.btn:disabled { opacity: 0.6; cursor: not-allowed; }
.meta { display: grid; grid-template-columns: 140px 1fr; gap: 0.5rem 1rem; background: #fff; border-radius: 12px; padding: 1.25rem 1.5rem; margin-bottom: 2rem; box-shadow: 0 1px 4px rgba(0,0,0,.06); }
dt { font-weight: 600; font-size: 0.85rem; color: #888; }
dd { font-size: 0.95rem; }
.digests h2 { font-size: 1.2rem; margin-bottom: 1rem; }
.digest-row { display: flex; justify-content: space-between; padding: 0.75rem 1rem; background: #fff; border-radius: 8px; margin-bottom: 0.5rem; box-shadow: 0 1px 3px rgba(0,0,0,.05); }
.digest-status { font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
.digest-status.sent { color: #1a6b1a; }
.digest-status.failed { color: #c0392b; }
.digest-status.generating, .digest-status.pending { color: #b07d00; }
.muted { color: #888; }
.status { text-align: center; padding: 4rem; color: #777; }
.capitalize { text-transform: capitalize; }
</style>
