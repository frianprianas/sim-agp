<template>
  <div class="page-wrapper">
    <Navbar />
    <div class="dashboard-layout">
      <aside class="sidebar">
        <div class="sidebar-header">
          <div class="logo">
            <svg width="40" height="40" viewBox="0 0 80 80" fill="none">
              <path d="M40 10L15 25V55L40 70L65 55V25L40 10Z" fill="url(#gradient1)" stroke="#fff" stroke-width="2"/>
              <defs>
                <linearGradient id="gradient1" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" style="stop-color:#667eea" />
                  <stop offset="100%" style="stop-color:#764ba2" />
                </linearGradient>
              </defs>
            </svg>
            <span>SIM AGP</span>
          </div>
        </div>

        <nav class="sidebar-nav">
          <router-link to="/dashboard" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
              <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"/>
            </svg>
            <span>Dashboard</span>
          </router-link>

          <router-link to="/mahasiswa" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"/>
            </svg>
            <span>Data Mahasiswa</span>
          </router-link>

          <router-link to="/prodi" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
              <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3z"/>
            </svg>
            <span>Program Studi</span>
          </router-link>

          <router-link v-if="authStore.isAdmin" to="/mahasiswa/create" class="nav-item" exact-active-class="active">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"/>
            </svg>
            <span>Tambah Mahasiswa</span>
          </router-link>

          <div class="nav-divider"></div>

          <router-link to="/profile" class="nav-item">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"/>
            </svg>
            <span>Profile</span>
          </router-link>
        </nav>

        <div class="sidebar-footer">
          <div class="user-info">
            <div class="user-avatar">
              {{ authStore.user?.name?.charAt(0)?.toUpperCase() }}
            </div>
            <div class="user-details">
              <div class="user-name">{{ authStore.user?.name }}</div>
              <div class="user-role">{{ authStore.user?.role }}</div>
            </div>
          </div>
        </div>
      </aside>

      <div class="main-content">
        <div class="container">
          <div class="form-header">
            <h1>{{ isEdit ? 'Edit' : 'Tambah' }} Mahasiswa</h1>
            <p>Form untuk {{ isEdit ? 'mengedit' : 'menambah' }} data mahasiswa</p>
          </div>

          <div class="card form-card">
            <div v-if="error" class="alert alert-danger">
              {{ error }}
            </div>

            <form @submit.prevent="handleSubmit">
          <div class="form-row">
            <div class="form-group">
              <label for="nim">NIM <span class="required">*</span></label>
              <input
                id="nim"
                v-model="form.nim"
                type="text"
                class="form-control"
                placeholder="Masukkan NIM"
                :disabled="isEdit || loading"
                required
              />
            </div>

            <div class="form-group">
              <label for="nama">Nama Lengkap <span class="required">*</span></label>
              <input
                id="nama"
                v-model="form.nama"
                type="text"
                class="form-control"
                placeholder="Masukkan nama lengkap"
                :disabled="loading"
                required
              />
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="tempat">Tempat Lahir <span class="required">*</span></label>
              <input
                id="tempat"
                v-model="form.tempat"
                type="text"
                class="form-control"
                placeholder="Masukkan tempat lahir"
                :disabled="loading"
                required
              />
            </div>

            <div class="form-group">
              <label for="tgl_lahir">Tanggal Lahir <span class="required">*</span></label>
              <input
                id="tgl_lahir"
                v-model="form.tgl_lahir"
                type="date"
                class="form-control"
                :disabled="loading"
                required
              />
            </div>
          </div>

          <div class="form-group">
            <label for="alamat">Alamat <span class="required">*</span></label>
            <textarea
              id="alamat"
              v-model="form.alamat"
              class="form-control"
              rows="3"
              placeholder="Masukkan alamat lengkap"
              :disabled="loading"
              required
            ></textarea>
          </div>

          <div class="form-group">
            <label for="jenis_kelamin">Jenis Kelamin <span class="required">*</span></label>
            <select
              id="jenis_kelamin"
              v-model="form.jenis_kelamin"
              class="form-control"
              :disabled="loading"
              required
            >
              <option value="">Pilih jenis kelamin</option>
              <option value="L">Laki-laki</option>
              <option value="P">Perempuan</option>
            </select>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="no_telepon">Telepon</label>
              <input
                id="no_telepon"
                v-model="form.no_telepon"
                type="tel"
                class="form-control"
                placeholder="Masukkan nomor telepon"
                :disabled="loading"
              />
            </div>

            <div class="form-group">
              <label for="email">Email</label>
              <input
                id="email"
                v-model="form.email"
                type="email"
                class="form-control"
                placeholder="Masukkan email"
                :disabled="loading"
              />
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="id_prodi">Program Studi <span class="required">*</span></label>
              <select
                id="id_prodi"
                v-model="form.id_prodi"
                class="form-control"
                :disabled="loading"
                required
              >
                <option value="">Pilih program studi</option>
                <option v-for="prodi in prodiList" :key="prodi.id_prodi" :value="prodi.id_prodi">
                  {{ prodi.prodi }} ({{ prodi.jenjang }})
                </option>
              </select>
            </div>

            <div class="form-group">
              <label for="tahun_masuk">Tahun Masuk <span class="required">*</span></label>
              <input
                id="tahun_masuk"
                v-model.number="form.tahun_masuk"
                type="number"
                class="form-control"
                placeholder="Masukkan tahun masuk"
                :disabled="loading"
                min="2000"
                :max="new Date().getFullYear()"
                required
              />
            </div>
          </div>

          <!-- Section Password (Only for Admin) -->
          <div v-if="authStore.isAdmin" class="password-section">
            <h3 class="section-title">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"/>
              </svg>
              Pengaturan Password
            </h3>
            <p class="section-desc">{{ isEdit ? 'Kosongkan jika tidak ingin mengubah password' : 'Password untuk login mahasiswa' }}</p>
            
            <div class="form-row">
              <div class="form-group">
                <label for="password">
                  Password 
                  <span v-if="!isEdit" class="required">*</span>
                </label>
                <input
                  id="password"
                  v-model="form.password"
                  type="password"
                  class="form-control"
                  placeholder="Masukkan password"
                  :disabled="loading"
                  :required="!isEdit"
                />
              </div>

              <div class="form-group">
                <label for="password_confirm">
                  Konfirmasi Password 
                  <span v-if="!isEdit" class="required">*</span>
                </label>
                <input
                  id="password_confirm"
                  v-model="form.password_confirm"
                  type="password"
                  class="form-control"
                  placeholder="Ulangi password"
                  :disabled="loading"
                  :required="!isEdit"
                />
              </div>
            </div>
          </div>

          <div class="form-actions">
            <router-link to="/mahasiswa" class="btn btn-secondary">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z"/>
              </svg>
              Kembali
            </router-link>
            <button type="submit" class="btn btn-primary" :disabled="loading">
              <span v-if="loading" class="loading-spinner"></span>
              <svg v-else width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"/>
              </svg>
              {{ loading ? 'Menyimpan...' : 'Simpan' }}
            </button>
          </div>
        </form>
      </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'
import { mahasiswaService, prodiService } from '../../services'
import Navbar from '../../components/Navbar.vue'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

const isEdit = computed(() => !!route.params.nim)
const loading = ref(false)
const error = ref('')
const prodiList = ref([])

const form = reactive({
  nim: '',
  nama: '',
  tempat: '',
  tgl_lahir: '',
  alamat: '',
  jenis_kelamin: '',
  no_telepon: '',
  email: '',
  id_prodi: '',
  tahun_masuk: new Date().getFullYear(),
  password: '',
  password_confirm: ''
})

const loadProdi = async () => {
  try {
    const response = await prodiService.getAll()
    prodiList.value = response.data || response.results || response
  } catch (err) {
    console.error('Error loading prodi:', err)
  }
}

const loadMahasiswa = async () => {
  if (!isEdit.value) return
  
  loading.value = true
  try {
    const response = await mahasiswaService.getById(route.params.nim)
    const data = response.data || response
    
    Object.keys(form).forEach(key => {
      if (data[key] !== undefined) {
        form[key] = data[key]
      }
    })
  } catch (err) {
    error.value = 'Gagal memuat data mahasiswa'
    console.error('Error loading mahasiswa:', err)
  } finally {
    loading.value = false
  }
}

const handleSubmit = async () => {
  loading.value = true
  error.value = ''
  
  // Validate password if admin is setting it
  if (authStore.isAdmin && form.password) {
    if (form.password !== form.password_confirm) {
      error.value = 'Password dan konfirmasi password tidak cocok'
      loading.value = false
      return
    }
    if (form.password.length < 6) {
      error.value = 'Password minimal 6 karakter'
      loading.value = false
      return
    }
  }
  
  // Validate password for new mahasiswa
  if (!isEdit.value && authStore.isAdmin && !form.password) {
    error.value = 'Password wajib diisi untuk mahasiswa baru'
    loading.value = false
    return
  }
  
  try {
    // Create data object without password_confirm
    const submitData = { ...form }
    delete submitData.password_confirm
    
    // Remove password if empty (for edit)
    if (isEdit.value && !submitData.password) {
      delete submitData.password
    }
    
    if (isEdit.value) {
      await mahasiswaService.update(form.nim, submitData)
    } else {
      await mahasiswaService.create(submitData)
    }
    router.push('/mahasiswa')
  } catch (err) {
    // Better error handling
    if (err.response?.data) {
      const errorData = err.response.data
      // If it's a validation error object
      if (typeof errorData === 'object' && !errorData.error) {
        const errors = Object.entries(errorData)
          .map(([key, value]) => `${key}: ${Array.isArray(value) ? value.join(', ') : value}`)
          .join('; ')
        error.value = errors
      } else {
        error.value = errorData.error || errorData.message || 'Gagal menyimpan data'
      }
    } else {
      error.value = err.message || 'Gagal menyimpan data'
    }
    console.error('Error saving mahasiswa:', err)
    console.error('Error response:', err.response?.data)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadProdi()
  loadMahasiswa()
})
</script>

<style scoped>
.page-wrapper {
  min-height: 100vh;
  background: #f3f4f6;
}

.dashboard-layout {
  display: flex;
  min-height: calc(100vh - 64px);
}

.sidebar {
  width: 280px;
  background: white;
  border-right: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 64px;
  left: 0;
  bottom: 0;
  overflow-y: auto;
  z-index: 40;
}

.sidebar-header {
  padding: 2rem 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
}

.sidebar-nav {
  flex: 1;
  padding: 1rem;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.875rem 1rem;
  color: #6b7280;
  text-decoration: none;
  border-radius: 10px;
  margin-bottom: 0.5rem;
  transition: all 0.3s;
  font-weight: 500;
}

.nav-item:hover {
  background: #f3f4f6;
  color: #667eea;
}

.nav-item.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.nav-divider {
  height: 1px;
  background: #e5e7eb;
  margin: 1rem 0;
}

.sidebar-footer {
  padding: 1.5rem;
  border-top: 1px solid #e5e7eb;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.125rem;
}

.user-details {
  flex: 1;
  min-width: 0;
}

.user-name {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.875rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.user-role {
  font-size: 0.75rem;
  color: #6b7280;
  text-transform: capitalize;
}

.main-content {
  flex: 1;
  margin-left: 280px;
  padding: 2rem;
}

.container {
  max-width: 900px;
  margin: 0 auto;
}

.form-header {
  margin-bottom: 2rem;
}

.form-header h1 {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
}

.form-header p {
  color: #6b7280;
  margin: 0;
}

.form-card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.password-section {
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 2px solid #e5e7eb;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.125rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
}

.section-title svg {
  color: #667eea;
}

.section-desc {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0 0 1.5rem 0;
}

.form-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-weight: 600;
  color: #374151;
  margin-bottom: 0.5rem;
  font-size: 0.875rem;
}

.required {
  color: #ef4444;
}

.form-control {
  width: 100%;
  padding: 0.875rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.3s;
}

.form-control:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}

.form-control:disabled {
  background-color: #f9fafb;
  cursor: not-allowed;
}

textarea.form-control {
  resize: vertical;
  min-height: 80px;
}

.form-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #e5e7eb;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.5rem;
  border-radius: 10px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
  text-decoration: none;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
}

.btn-secondary {
  background: #f3f4f6;
  color: #6b7280;
}

.btn-secondary:hover {
  background: #e5e7eb;
}

.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.loading-spinner {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.alert {
  padding: 1rem 1.25rem;
  border-radius: 10px;
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
}

.alert-danger {
  background: #fef2f2;
  color: #991b1b;
  border: 1px solid #fecaca;
}

@media (max-width: 1024px) {
  .sidebar {
    transform: translateX(-100%);
  }

  .main-content {
    margin-left: 0;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding: 1rem;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  .form-card {
    padding: 1.5rem;
  }

  .form-actions {
    flex-direction: column-reverse;
  }

  .btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
