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

          <router-link to="/prodi" class="nav-item" exact-active-class="active">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
              <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3z"/>
            </svg>
            <span>Program Studi</span>
          </router-link>

          <router-link v-if="authStore.isAdmin" to="/mahasiswa/create" class="nav-item">
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
          <div class="page-header">
            <div>
              <h1>Program Studi</h1>
              <p>Daftar program studi yang tersedia</p>
            </div>
            <router-link v-if="authStore.isAdmin" to="/prodi/create" class="btn btn-primary">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"/>
              </svg>
              Tambah Prodi
            </router-link>
          </div>

          <div v-if="loading" class="loading-card">
            <div class="loading-spinner"></div>
            <p>Memuat data...</p>
          </div>

          <div v-else-if="error" class="alert alert-danger">
            {{ error }}
          </div>

          <div v-else-if="prodiList.length === 0" class="empty-state">
            <svg width="120" height="120" viewBox="0 0 120 120" fill="none">
              <circle cx="60" cy="60" r="60" fill="#f3f4f6"/>
              <path d="M60 30L30 45V75L60 90L90 75V45L60 30Z" fill="#e5e7eb"/>
            </svg>
            <h3>Belum ada data program studi</h3>
            <p>Tambahkan program studi pertama Anda</p>
            <router-link v-if="authStore.isAdmin" to="/prodi/create" class="btn btn-primary">
              Tambah Prodi
            </router-link>
          </div>

          <div v-else class="prodi-grid">
            <div v-for="prodi in prodiList" :key="prodi.id_prodi" class="prodi-card">
              <div class="prodi-icon">
                <svg width="40" height="40" viewBox="0 0 40 40" fill="currentColor">
                  <path d="M20 5L5 12.5V27.5L20 35L35 27.5V12.5L20 5Z"/>
                </svg>
              </div>
              <div class="prodi-info">
                <h3>{{ prodi.prodi }}</h3>
                <span class="jenjang-badge">{{ prodi.jenjang }}</span>
              </div>
              <div v-if="authStore.isAdmin" class="prodi-actions">
                <router-link :to="`/prodi/edit/${prodi.id_prodi}`" class="btn-icon btn-edit" title="Edit">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"/>
                  </svg>
                </router-link>
                <button @click="handleDelete(prodi)" class="btn-icon btn-delete" title="Hapus">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../../stores/auth'
import { prodiService } from '../../services'
import Navbar from '../../components/Navbar.vue'

const authStore = useAuthStore()

const prodiList = ref([])
const loading = ref(false)
const error = ref('')

const loadProdi = async () => {
  loading.value = true
  error.value = ''
  try {
    const response = await prodiService.getAll()
    const data = response.data || response.results || response || []
    prodiList.value = Array.isArray(data) ? data : []
  } catch (err) {
    error.value = 'Gagal memuat data program studi'
    console.error('Error loading prodi:', err)
  } finally {
    loading.value = false
  }
}

const handleDelete = async (prodi) => {
  if (!confirm(`Apakah Anda yakin ingin menghapus program studi "${prodi.prodi}"?`)) {
    return
  }

  try {
    await prodiService.delete(prodi.id_prodi)
    await loadProdi()
  } catch (err) {
    alert('Gagal menghapus program studi')
    console.error('Error deleting prodi:', err)
  }
}

onMounted(() => {
  loadProdi()
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
  max-width: 1400px;
  margin: 0 auto;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
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

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
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

.alert {
  padding: 1rem 1.25rem;
  border-radius: 10px;
  font-size: 0.875rem;
}

.alert-danger {
  background: #fef2f2;
  color: #991b1b;
  border: 1px solid #fecaca;
}

.empty-state {
  background: white;
  border-radius: 16px;
  padding: 4rem 2rem;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.empty-state svg {
  margin-bottom: 1.5rem;
}

.empty-state h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
}

.empty-state p {
  color: #6b7280;
  margin: 0 0 1.5rem 0;
}

.prodi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.prodi-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.prodi-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.prodi-icon {
  width: 64px;
  height: 64px;
  border-radius: 12px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}

.prodi-info {
  flex: 1;
}

.prodi-info h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
}

.jenjang-badge {
  display: inline-block;
  padding: 0.375rem 0.75rem;
  background: #f3f4f6;
  color: #6b7280;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 600;
}

.prodi-actions {
  display: flex;
  gap: 0.5rem;
  padding-top: 1rem;
  border-top: 1px solid #e5e7eb;
}

.btn-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: all 0.3s;
  text-decoration: none;
}

.btn-edit {
  background: #eff6ff;
  color: #2563eb;
}

.btn-edit:hover {
  background: #dbeafe;
}

.btn-delete {
  background: #fef2f2;
  color: #dc2626;
}

.btn-delete:hover {
  background: #fee2e2;
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

  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .btn {
    width: 100%;
    justify-content: center;
  }

  .prodi-grid {
    grid-template-columns: 1fr;
  }
}
</style>
