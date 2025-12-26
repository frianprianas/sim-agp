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

          <!-- Admin Only Menu -->
          <template v-if="authStore.isAdmin">
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

            <router-link to="/mahasiswa/create" class="nav-item">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"/>
              </svg>
              <span>Tambah Mahasiswa</span>
            </router-link>

            <div class="nav-divider"></div>

            <router-link to="/profile" class="nav-item" exact-active-class="active">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"/>
              </svg>
              <span>Profile</span>
            </router-link>
          </template>

          <!-- Mahasiswa Only Menu -->
          <template v-else>
            <router-link to="/profile" class="nav-item" exact-active-class="active">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z"/>
              </svg>
              <span>Ubah Email & Password</span>
            </router-link>
          </template>
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
          <div class="page-header">
            <h1>Profile</h1>
            <p>Informasi akun Anda</p>
          </div>

          <div v-if="loading" class="loading-card">
            <div class="loading-spinner"></div>
            <p>Memuat data...</p>
          </div>

          <div v-else class="card">
            <div class="profile-header">
              <div class="profile-avatar">
                {{ user?.name?.charAt(0).toUpperCase() }}
              </div>
              <div class="profile-info">
                <h2>{{ user?.name }}</h2>
                <p class="role-badge">{{ user?.role === 'admin' ? 'Administrator' : 'Mahasiswa' }}</p>
              </div>
            </div>

            <div class="profile-details">
              <div class="detail-item">
                <strong>Username:</strong>
                <span>{{ user?.username }}</span>
              </div>
              <div class="detail-item">
                <strong>Email:</strong>
                <span>{{ user?.email || '-' }}</span>
              </div>
              <div class="detail-item">
                <strong>Role:</strong>
                <span>{{ user?.role === 'admin' ? 'Administrator' : 'Mahasiswa' }}</span>
              </div>
              <div v-if="user?.mahasiswa_detail" class="detail-item">
                <strong>NIM:</strong>
                <span>{{ user?.mahasiswa_detail?.nim }}</span>
              </div>
              <div v-if="user?.mahasiswa_detail" class="detail-item">
                <strong>Program Studi:</strong>
                <span>{{ user?.mahasiswa_detail?.prodi_detail?.prodi }}</span>
              </div>
            </div>

            <!-- Edit Form for Mahasiswa -->
            <div v-if="!authStore.isAdmin" class="edit-section">
              <h3 class="section-title">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"/>
                </svg>
                Ubah Data
              </h3>

              <div v-if="success" class="alert alert-success">{{ success }}</div>
              <div v-if="error" class="alert alert-danger">{{ error }}</div>

              <form @submit.prevent="handleUpdate">
                <div class="form-group">
                  <label for="email">Email</label>
                  <input
                    id="email"
                    v-model="form.email"
                    type="email"
                    class="form-control"
                    placeholder="Masukkan email"
                    :disabled="updating"
                  />
                </div>

                <div class="form-group">
                  <label for="password">Password Baru</label>
                  <input
                    id="password"
                    v-model="form.password"
                    type="password"
                    class="form-control"
                    placeholder="Kosongkan jika tidak ingin mengubah"
                    :disabled="updating"
                  />
                  <small class="form-hint">Minimal 6 karakter</small>
                </div>

                <div class="form-group">
                  <label for="password_confirm">Konfirmasi Password Baru</label>
                  <input
                    id="password_confirm"
                    v-model="form.password_confirm"
                    type="password"
                    class="form-control"
                    placeholder="Ulangi password baru"
                    :disabled="updating"
                  />
                </div>

                <button type="submit" class="btn btn-primary" :disabled="updating">
                  <span v-if="updating" class="loading-spinner"></span>
                  <svg v-else width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"/>
                  </svg>
                  {{ updating ? 'Menyimpan...' : 'Simpan Perubahan' }}
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { authService } from '@/services'
import Navbar from '@/components/Navbar.vue'

const authStore = useAuthStore()
const user = ref(null)
const loading = ref(true)
const updating = ref(false)
const success = ref('')
const error = ref('')

const form = reactive({
  email: '',
  password: '',
  password_confirm: ''
})

const handleUpdate = async () => {
  success.value = ''
  error.value = ''

  if (form.password && form.password !== form.password_confirm) {
    error.value = 'Password dan konfirmasi password tidak cocok'
    return
  }

  if (form.password && form.password.length < 6) {
    error.value = 'Password minimal 6 karakter'
    return
  }

  updating.value = true
  try {
    const updateData = {}
    if (form.email) updateData.email = form.email
    if (form.password) updateData.password = form.password

    await authService.updateProfile(updateData)
    success.value = 'Data berhasil diperbarui'
    
    // Reload profile
    await authStore.fetchProfile()
    user.value = authStore.user
    form.email = user.value?.email || ''
    form.password = ''
    form.password_confirm = ''
  } catch (err) {
    error.value = err.response?.data?.error || 'Gagal memperbarui data'
    console.error('Error updating profile:', err)
  } finally {
    updating.value = false
  }
}

onMounted(async () => {
  try {
    loading.value = true
    await authStore.fetchProfile()
    user.value = authStore.user
    form.email = user.value?.email || ''
  } catch (error) {
    console.error('Error loading profile:', error)
  } finally {
    loading.value = false
  }
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

.page-header {
  margin-bottom: 2rem;
}

.page-header h1 {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
}

.page-header p {
  color: #6b7280;
  margin: 0;
}

.card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.loading-card {
  background: white;
  border-radius: 16px;
  padding: 4rem 2rem;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.loading-spinner {
  display: inline-block;
  width: 48px;
  height: 48px;
  border: 4px solid #f3f4f6;
  border-top-color: #667eea;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-card p {
  color: #6b7280;
  margin: 0;
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 2rem;
  padding-bottom: 2rem;
  border-bottom: 2px solid #e5e7eb;
  margin-bottom: 2rem;
}

.profile-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  font-weight: bold;
}

.profile-info h2 {
  margin: 0 0 0.5rem 0;
  color: #1f2937;
  font-size: 1.75rem;
}

.role-badge {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.375rem 1rem;
  border-radius: 1rem;
  display: inline-block;
  font-size: 0.875rem;
  font-weight: 600;
}

.profile-details {
  display: grid;
  gap: 1rem;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  background: #f9fafb;
  border-radius: 10px;
  border: 1px solid #e5e7eb;
}

.detail-item strong {
  color: #374151;
  font-weight: 600;
}

.detail-item span {
  color: #6b7280;
}

.edit-section {
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 2px solid #e5e7eb;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 1.5rem 0;
}

.section-title svg {
  color: #667eea;
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

.form-hint {
  display: block;
  margin-top: 0.25rem;
  font-size: 0.75rem;
  color: #6b7280;
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

.alert-success {
  background: #f0fdf4;
  color: #166534;
  border: 1px solid #bbf7d0;
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

  .profile-header {
    flex-direction: column;
    text-align: center;
  }

  .detail-item {
    flex-direction: column;
    gap: 0.5rem;
  }
}
</style>
