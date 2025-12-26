import api from './api'

export const authService = {
  async login(username, password) {
    const response = await api.post('/api/auth/login/', { username, password })
    if (response.data.token) {
      localStorage.setItem('token', response.data.token)
      localStorage.setItem('user', JSON.stringify(response.data.user))
    }
    return response.data
  },

  async register(userData) {
    const response = await api.post('/api/auth/register/', userData)
    if (response.data.token) {
      localStorage.setItem('token', response.data.token)
      localStorage.setItem('user', JSON.stringify(response.data.user))
    }
    return response.data
  },

  async logout() {
    try {
      await api.post('/api/auth/logout/')
    } finally {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
    }
  },

  async getProfile() {
    const response = await api.get('/api/auth/profile/')
    return response.data
  },

  async updateProfile(data) {
    const response = await api.put('/api/auth/update-profile/', data)
    if (response.data.user) {
      localStorage.setItem('user', JSON.stringify(response.data.user))
    }
    return response.data
  },

  isAuthenticated() {
    return !!localStorage.getItem('token')
  },

  getCurrentUser() {
    const user = localStorage.getItem('user')
    return user ? JSON.parse(user) : null
  },
}

export const prodiService = {
  async getAll() {
    const response = await api.get('/api/prodi/')
    return response.data
  },

  async getById(id) {
    const response = await api.get(`/api/prodi/${id}/`)
    return response.data
  },

  async create(data) {
    const response = await api.post('/api/prodi/', data)
    return response.data
  },

  async update(id, data) {
    const response = await api.put(`/api/prodi/${id}/`, data)
    return response.data
  },

  async delete(id) {
    const response = await api.delete(`/api/prodi/${id}/`)
    return response.data
  },

  async getByJenjang(jenjang) {
    const response = await api.get(`/api/prodi/by_jenjang/?jenjang=${jenjang}`)
    return response.data
  },
}

export const mahasiswaService = {
  async getAll() {
    const response = await api.get('/api/mahasiswa/')
    return response.data
  },

  async getById(nim) {
    const response = await api.get(`/api/mahasiswa/${nim}/`)
    return response.data
  },

  async create(data) {
    const response = await api.post('/api/mahasiswa/', data)
    return response.data
  },

  async update(nim, data) {
    const response = await api.put(`/api/mahasiswa/${nim}/`, data)
    return response.data
  },

  async delete(nim) {
    const response = await api.delete(`/api/mahasiswa/${nim}/`)
    return response.data
  },

  async getByProdi(idProdi) {
    const response = await api.get(`/api/mahasiswa/by_prodi/?id_prodi=${idProdi}`)
    return response.data
  },

  async getByTahun(tahun) {
    const response = await api.get(`/api/mahasiswa/by_tahun/?tahun=${tahun}`)
    return response.data
  },
}

export const userService = {
  async getAll() {
    const response = await api.get('/api/users/')
    return response.data
  },

  async getById(id) {
    const response = await api.get(`/api/users/${id}/`)
    return response.data
  },

  async update(id, data) {
    const response = await api.put(`/api/users/${id}/`, data)
    return response.data
  },

  async delete(id) {
    const response = await api.delete(`/api/users/${id}/`)
    return response.data
  },

  async getByRole(role) {
    const response = await api.get(`/api/users/by_role/?role=${role}`)
    return response.data
  },
}
