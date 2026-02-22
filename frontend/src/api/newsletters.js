import client from './client'

export const newsletters = {
  list: () => client.get('/newsletters/'),
  get: (id) => client.get(`/newsletters/${id}/`),
  create: (data) => client.post('/newsletters/', data),
  update: (id, data) => client.patch(`/newsletters/${id}/`, data),
  remove: (id) => client.delete(`/newsletters/${id}/`),
  trigger: (id) => client.post(`/newsletters/${id}/trigger/`),
  digests: (id) => client.get(`/newsletters/${id}/digests/`),
}
