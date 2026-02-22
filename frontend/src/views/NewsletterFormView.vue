<template>
  <div class="layout">
    <AppNav />
    <main class="form-page">
      <h1>{{ isEdit ? 'Edit newsletter' : 'New newsletter' }}</h1>
      <p v-if="error" class="form-error">{{ error }}</p>

      <form @submit.prevent="submit">
        <label>
          Name
          <input v-model="form.name" type="text" required placeholder="e.g. AI Research Weekly" />
        </label>
        <label>
          Topic
          <textarea
            v-model="form.topic"
            required
            rows="4"
            placeholder="Describe the topics you want covered. Be specific — the more detail, the better the digest."
          />
        </label>
        <label>
          Delivery cadence
          <select v-model="form.cadence">
            <option value="daily">Daily</option>
            <option value="weekly">Weekly</option>
            <option value="biweekly">Bi-weekly</option>
            <option value="monthly">Monthly</option>
          </select>
        </label>
        <label class="checkbox-label" v-if="isEdit">
          <input v-model="form.is_active" type="checkbox" />
          Active
        </label>
        <div class="form-actions">
          <RouterLink to="/dashboard" class="btn btn-ghost">Cancel</RouterLink>
          <button type="submit" :disabled="loading" class="btn btn-primary">
            {{ loading ? 'Saving…' : isEdit ? 'Save changes' : 'Create' }}
          </button>
        </div>
      </form>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute, RouterLink } from 'vue-router'
import { useNewslettersStore } from '@/stores/newsletters'
import AppNav from '@/components/AppNav.vue'

const router = useRouter()
const route = useRoute()
const store = useNewslettersStore()

const isEdit = computed(() => !!route.params.id)
const loading = ref(false)
const error = ref('')

const form = ref({
  name: '',
  topic: '',
  cadence: 'weekly',
  is_active: true,
})

onMounted(async () => {
  if (isEdit.value) {
    await store.fetchOne(route.params.id)
    const n = store.current
    form.value = { name: n.name, topic: n.topic, cadence: n.cadence, is_active: n.is_active }
  }
})

async function submit() {
  loading.value = true
  error.value = ''
  try {
    if (isEdit.value) {
      await store.update(route.params.id, form.value)
    } else {
      const created = await store.create(form.value)
      router.push(`/newsletters/${created.id}`)
      return
    }
    router.push('/dashboard')
  } catch (e) {
    const data = e.response?.data
    error.value = data ? Object.values(data).flat().join(' ') : 'Save failed.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.layout { min-height: 100vh; display: flex; flex-direction: column; }
.form-page { max-width: 600px; margin: 0 auto; padding: 2rem 1.5rem; width: 100%; }
h1 { margin-bottom: 1.5rem; font-size: 1.8rem; }
form { display: flex; flex-direction: column; gap: 1.2rem; }
label { display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.9rem; font-weight: 500; }
input, textarea, select { padding: 0.65rem 0.9rem; border: 1.5px solid #ddd; border-radius: 8px; font-size: 1rem; font-family: inherit; outline: none; transition: border-color 0.15s; }
input:focus, textarea:focus, select:focus { border-color: #1a1a1a; }
.checkbox-label { flex-direction: row; align-items: center; gap: 0.5rem; }
.form-actions { display: flex; gap: 1rem; justify-content: flex-end; margin-top: 0.5rem; }
.btn { padding: 0.65rem 1.5rem; border-radius: 8px; font-size: 0.95rem; font-weight: 600; cursor: pointer; border: none; }
.btn-primary { background: #1a1a1a; color: #fff; }
.btn-ghost { background: transparent; color: #1a1a1a; border: 2px solid #1a1a1a; }
.btn:disabled { opacity: 0.6; cursor: not-allowed; }
.form-error { color: #c0392b; font-size: 0.9rem; margin-bottom: 0.5rem; }
</style>
