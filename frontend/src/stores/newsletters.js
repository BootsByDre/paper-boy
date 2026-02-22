import { defineStore } from 'pinia'
import { ref } from 'vue'
import { newsletters as api } from '@/api/newsletters'

export const useNewslettersStore = defineStore('newsletters', () => {
  const items = ref([])
  const current = ref(null)
  const digests = ref([])
  const loading = ref(false)
  const error = ref(null)

  async function fetchAll() {
    loading.value = true
    error.value = null
    try {
      const { data } = await api.list()
      items.value = data.results ?? data
    } catch (e) {
      error.value = e.response?.data ?? e.message
    } finally {
      loading.value = false
    }
  }

  async function fetchOne(id) {
    loading.value = true
    error.value = null
    try {
      const { data } = await api.get(id)
      current.value = data
    } catch (e) {
      error.value = e.response?.data ?? e.message
    } finally {
      loading.value = false
    }
  }

  async function create(payload) {
    const { data } = await api.create(payload)
    items.value.unshift(data)
    return data
  }

  async function update(id, payload) {
    const { data } = await api.update(id, payload)
    const idx = items.value.findIndex((n) => n.id === id)
    if (idx !== -1) items.value[idx] = data
    current.value = data
    return data
  }

  async function remove(id) {
    await api.remove(id)
    items.value = items.value.filter((n) => n.id !== id)
  }

  async function trigger(id) {
    return api.trigger(id)
  }

  async function fetchDigests(newsletterId) {
    const { data } = await api.digests(newsletterId)
    digests.value = data.results ?? data
  }

  return {
    items,
    current,
    digests,
    loading,
    error,
    fetchAll,
    fetchOne,
    create,
    update,
    remove,
    trigger,
    fetchDigests,
  }
})
