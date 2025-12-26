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
              <h1>Detail Mahasiswa</h1>
              <p>Informasi lengkap mahasiswa</p>
            </div>
            <div class="header-actions">
              <router-link to="/mahasiswa" class="btn btn-secondary">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z"/>
                </svg>
                Kembali
              </router-link>
              <router-link v-if="authStore.isAdmin && mahasiswa" :to="`/mahasiswa/${mahasiswa.nim}/edit`" class="btn btn-primary">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"/>
                </svg>
                Edit
              </router-link>
            </div>
          </div>

          <div v-if="loading" class="loading-card">
            <div class="loading-spinner"></div>
            <p>Memuat data...</p>
          </div>

          <div v-else-if="error" class="alert alert-danger">{{ error }}</div>

          <div v-else-if="mahasiswa" class="detail-card">
            <div class="profile-section">
              <div class="profile-avatar">
                {{ mahasiswa.nama?.charAt(0)?.toUpperCase() }}
              </div>
              <div class="profile-info">
                <h2>{{ mahasiswa.nama }}</h2>
                <p class="nim-badge">{{ mahasiswa.nim }}</p>
              </div>
            </div>

            <div class="info-grid">
              <div class="info-item">
                <div class="info-label">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"/>
                  </svg>
                  Jenis Kelamin
                </div>
                <div class="info-value">{{ mahasiswa.jenis_kelamin === 'L' ? 'Laki-laki' : 'Perempuan' }}</div>
              </div>

              <div class="info-item">
                <div class="info-label">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"/>
                  </svg>
                  Tempat, Tanggal Lahir
                </div>
                <div class="info-value">{{ mahasiswa.tempat }}, {{ formatDate(mahasiswa.tgl_lahir) }}</div>
              </div>

              <div class="info-item full-width">
                <div class="info-label">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z"/>
                  </svg>
                  Alamat
                </div>
                <div class="info-value">{{ mahasiswa.alamat }}</div>
              </div>

              <div class="info-item">
                <div class="info-label">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/>
                  </svg>
                  Telepon
                </div>
                <div class="info-value">{{ mahasiswa.no_telepon || '-' }}</div>
              </div>

              <div class="info-item">
                <div class="info-label">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"/>
                    <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"/>
                  </svg>
                  Email
                </div>
                <div class="info-value">{{ mahasiswa.email || '-' }}</div>
              </div>

              <div class="info-item">
                <div class="info-label">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3z"/>
                  </svg>
                  Program Studi
                </div>
                <div class="info-value">{{ mahasiswa.prodi_detail?.prodi }} ({{ mahasiswa.prodi_detail?.jenjang }})</div>
              </div>

              <div class="info-item">
                <div class="info-label">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"/>
                  </svg>
                  Tahun Masuk
                </div>
                <div class="info-value">{{ mahasiswa.tahun_masuk }}</div>
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
import { useRoute } from 'vue-router'
import { useAuthStore } from '../../stores/auth'
import { mahasiswaService } from '../../services'
import Navbar from '../../components/Navbar.vue'

const route = useRoute()
const authStore = useAuthStore()

const mahasiswa = ref(null)
const loading = ref(false)
const error = ref('')

const formatDate = (dateString) => {
  if (!dateString) return '-'
  const date = new Date(dateString)
  return date.toLocaleDateString('id-ID', { 
    day: 'numeric', 
    month: 'long', 
    year: 'numeric' 
  })
}

const loadMahasiswa = async () => {
  loading.value = true
  error.value = ''
  try {
    const response = await mahasiswaService.getById(route.params.nim)
    mahasiswa.value = response.data || response
  } catch (err) {
    error.value = 'Gagal memuat data mahasiswa'
    console.error('Error loading mahasiswa:', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
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
  max-width: 1000px;
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

.header-actions {
  display: flex;
  gap: 1rem;
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

.btn-secondary {
  background: #f3f4f6;
  color: #6b7280;
}

.btn-secondary:hover {
  background: #e5e7eb;
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

.detail-card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.profile-section {
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

.nim-badge {
  background: #f3f4f6;
  color: #6b7280;
  padding: 0.375rem 1rem;
  border-radius: 8px;
  display: inline-block;
  font-size: 0.875rem;
  font-weight: 600;
  margin: 0;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.info-item {
  padding: 1.5rem;
  background: #f9fafb;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
}

.info-item.full-width {
  grid-column: 1 / -1;
}

.info-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  color: #374151;
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
}

.info-label svg {
  color: #667eea;
}

.info-value {
  color: #6b7280;
  font-size: 1rem;
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

  .header-actions {
    width: 100%;
    flex-direction: column;
  }

  .btn {
    width: 100%;
    justify-content: center;
  }

  .profile-section {
    flex-direction: column;
    text-align: center;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }
}
</style>
