<template>
  <div class="dashboard-wrapper">
    <Navbar />
    <div class="dashboard-layout">
      <!-- Sidebar -->
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
          <router-link to="/dashboard" class="nav-item" exact-active-class="active">
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

            <router-link to="/profile" class="nav-item">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"/>
              </svg>
              <span>Profile</span>
            </router-link>
          </template>

          <!-- Mahasiswa Only Menu -->
          <template v-else>
            <router-link to="/profile" class="nav-item">
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

      <!-- Main Content -->
      <div class="dashboard-container">
      <div class="dashboard-header">
        <div class="header-content">
          <div class="greeting">
            <h1>Selamat Datang Kembali! 👋</h1>
            <p>{{ authStore.user?.name }} - <span class="role-badge">{{ authStore.user?.role }}</span></p>
          </div>
          <div class="header-actions">
            <div class="date-info">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"/>
              </svg>
              {{ currentDate }}
            </div>
          </div>
        </div>
      </div>

      <div class="dashboard-content">
        <!-- Admin Dashboard -->
        <div v-if="authStore.isAdmin">
          <!-- Statistics Cards -->
          <div class="stats-grid">
          <div class="stat-card" :class="loading ? 'loading' : ''">
            <div class="stat-icon-wrapper gradient-blue">
              <svg width="32" height="32" viewBox="0 0 20 20" fill="currentColor">
                <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"/>
              </svg>
            </div>
            <div class="stat-content">
              <div class="stat-label">Total Mahasiswa</div>
              <div class="stat-value">{{ stats.totalMahasiswa }}</div>
              <div class="stat-change positive">
                <svg width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z"/>
                </svg>
                <span>Aktif</span>
              </div>
            </div>
          </div>

          <div class="stat-card" :class="loading ? 'loading' : ''">
            <div class="stat-icon-wrapper gradient-purple">
              <svg width="32" height="32" viewBox="0 0 20 20" fill="currentColor">
                <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3zM3.31 9.397L5 10.12v4.102a8.969 8.969 0 00-1.05-.174 1 1 0 01-.89-.89 11.115 11.115 0 01.25-3.762zM9.3 16.573A9.026 9.026 0 007 14.935v-3.957l1.818.78a3 3 0 002.364 0l5.508-2.361a11.026 11.026 0 01.25 3.762 1 1 0 01-.89.89 8.968 8.968 0 00-5.35 2.524 1 1 0 01-1.4 0zM6 18a1 1 0 001-1v-2.065a8.935 8.935 0 00-2-.712V17a1 1 0 001 1z"/>
              </svg>
            </div>
            <div class="stat-content">
              <div class="stat-label">Program Studi</div>
              <div class="stat-value">{{ stats.totalProdi }}</div>
              <div class="stat-change">
                <span>6 Program</span>
              </div>
            </div>
          </div>

          <div class="stat-card" :class="loading ? 'loading' : ''">
            <div class="stat-icon-wrapper gradient-green">
              <svg width="32" height="32" viewBox="0 0 20 20" fill="currentColor">
                <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z"/>
              </svg>
            </div>
            <div class="stat-content">
              <div class="stat-label">Total Users</div>
              <div class="stat-value">{{ stats.totalUsers }}</div>
              <div class="stat-change">
                <span>Terdaftar</span>
              </div>
            </div>
          </div>

          <div class="stat-card" :class="loading ? 'loading' : ''">
            <div class="stat-icon-wrapper gradient-orange">
              <svg width="32" height="32" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"/>
              </svg>
            </div>
            <div class="stat-content">
              <div class="stat-label">Tahun Akademik</div>
              <div class="stat-value">2025</div>
              <div class="stat-change positive">
                <span>Aktif</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Actions -->
        <div class="quick-actions-section">
          <div class="section-header">
            <h2>Quick Actions</h2>
            <p>Akses cepat ke fitur utama</p>
          </div>
          <div class="action-cards">
            <router-link to="/mahasiswa" class="action-card">
              <div class="action-icon gradient-blue">
                <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"/>
                </svg>
              </div>
              <div class="action-content">
                <h3>Data Mahasiswa</h3>
                <p>Kelola data mahasiswa</p>
              </div>
              <div class="action-arrow">→</div>
            </router-link>

            <router-link to="/prodi" class="action-card">
              <div class="action-icon gradient-purple">
                <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3z"/>
                </svg>
              </div>
              <div class="action-content">
                <h3>Program Studi</h3>
                <p>Lihat program studi</p>
              </div>
              <div class="action-arrow">→</div>
            </router-link>

            <router-link v-if="authStore.isAdmin" to="/mahasiswa/create" class="action-card">
              <div class="action-icon gradient-green">
                <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"/>
                </svg>
              </div>
              <div class="action-content">
                <h3>Tambah Mahasiswa</h3>
                <p>Tambah data baru</p>
              </div>
              <div class="action-arrow">→</div>
            </router-link>

            <router-link to="/profile" class="action-card">
              <div class="action-icon gradient-orange">
                <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z"/>
                </svg>
              </div>
              <div class="action-content">
                <h3>Profile</h3>
                <p>Lihat profile anda</p>
              </div>
              <div class="action-arrow">→</div>
            </router-link>
          </div>
        </div>

        <!-- Recent Activity -->
        <div class="recent-activity">
          <div class="section-header">
            <h2>Informasi Sistem</h2>
            <p>Status dan informasi terkini</p>
          </div>
          <div class="activity-card">
            <div class="activity-items">
              <div class="activity-item">
                <div class="activity-icon success">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"/>
                  </svg>
                </div>
                <div class="activity-content">
                  <h4>Sistem Berjalan Normal</h4>
                  <p>Semua layanan berfungsi dengan baik</p>
                </div>
                <div class="activity-time">Aktif</div>
              </div>

              <div class="activity-item">
                <div class="activity-icon info">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"/>
                  </svg>
                </div>
                <div class="activity-content">
                  <h4>Database PostgreSQL</h4>
                  <p>Koneksi database stabil dan optimal</p>
                </div>
                <div class="activity-time">Online</div>
              </div>

              <div class="activity-item">
                <div class="activity-icon success">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"/>
                  </svg>
                </div>
                <div class="activity-content">
                  <h4>Keamanan Terjaga</h4>
                  <p>Autentikasi dan otorisasi aktif</p>
                </div>
                <div class="activity-time">Aman</div>
              </div>
            </div>
          </div>
        </div>
        </div>

        <!-- Mahasiswa Dashboard -->
        <div v-else>
          <div class="mahasiswa-profile-card">
            <div class="profile-header-section">
              <div class="large-avatar">
                {{ authStore.user?.name?.charAt(0)?.toUpperCase() }}
              </div>
              <div class="profile-info-section">
                <h2>{{ authStore.user?.name }}</h2>
                <p class="nim-text">NIM: {{ mahasiswaData?.nim }}</p>
                <p class="prodi-text">{{ mahasiswaData?.prodi_detail?.prodi }} ({{ mahasiswaData?.prodi_detail?.jenjang }})</p>
              </div>
            </div>

            <div class="profile-details-grid">
              <div class="detail-box">
                <div class="detail-icon">
                  <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"/>
                    <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"/>
                  </svg>
                </div>
                <div class="detail-content">
                  <div class="detail-label">Email</div>
                  <div class="detail-value">{{ mahasiswaData?.email || '-' }}</div>
                </div>
              </div>

              <div class="detail-box">
                <div class="detail-icon">
                  <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/>
                  </svg>
                </div>
                <div class="detail-content">
                  <div class="detail-label">Telepon</div>
                  <div class="detail-value">{{ mahasiswaData?.no_telepon || '-' }}</div>
                </div>
              </div>

              <div class="detail-box">
                <div class="detail-icon">
                  <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z"/>
                  </svg>
                </div>
                <div class="detail-content">
                  <div class="detail-label">Tempat, Tanggal Lahir</div>
                  <div class="detail-value">{{ mahasiswaData?.tempat }}, {{ formatDate(mahasiswaData?.tgl_lahir) }}</div>
                </div>
              </div>

              <div class="detail-box">
                <div class="detail-icon">
                  <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"/>
                  </svg>
                </div>
                <div class="detail-content">
                  <div class="detail-label">Tahun Masuk</div>
                  <div class="detail-value">{{ mahasiswaData?.tahun_masuk }}</div>
                </div>
              </div>

              <div class="detail-box full-width">
                <div class="detail-icon">
                  <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z"/>
                  </svg>
                </div>
                <div class="detail-content">
                  <div class="detail-label">Alamat</div>
                  <div class="detail-value">{{ mahasiswaData?.alamat }}</div>
                </div>
              </div>
            </div>

            <div class="action-buttons">
              <router-link to="/profile" class="btn btn-primary">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"/>
                </svg>
                Ubah Email & Password
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useAuthStore } from '../stores/auth'
import { mahasiswaService, prodiService, userService } from '../services'
import Navbar from '../components/Navbar.vue'

const authStore = useAuthStore()
const loading = ref(false)
const mahasiswaData = ref(null)
const stats = ref({
  totalMahasiswa: 0,
  totalProdi: 0,
  totalUsers: 0
})

const formatDate = (dateString) => {
  if (!dateString) return '-'
  const date = new Date(dateString)
  return date.toLocaleDateString('id-ID', { 
    day: 'numeric', 
    month: 'long', 
    year: 'numeric' 
  })
}

const currentDate = computed(() => {
  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
  return new Date().toLocaleDateString('id-ID', options)
})

const loadMahasiswaData = async () => {
  if (!authStore.user?.nim) return
  
  try {
    const response = await mahasiswaService.getById(authStore.user.nim.nim || authStore.user.nim)
    mahasiswaData.value = response.data || response
  } catch (err) {
    console.error('Error loading mahasiswa data:', err)
  }
}

const loadStats = async () => {
  loading.value = true
  try {
    const [mahasiswaRes, prodiRes, usersRes] = await Promise.all([
      mahasiswaService.getAll(),
      prodiService.getAll(),
      userService.getAll()
    ])
    
    // Handle different response structures
    const mahasiswaData = mahasiswaRes.data || mahasiswaRes.results || mahasiswaRes || []
    const prodiData = prodiRes.data || prodiRes.results || prodiRes || []
    const usersData = usersRes.data || usersRes.results || usersRes || []
    
    stats.value = {
      totalMahasiswa: Array.isArray(mahasiswaData) ? mahasiswaData.length : mahasiswaData.count || 0,
      totalProdi: Array.isArray(prodiData) ? prodiData.length : prodiData.count || 0,
      totalUsers: Array.isArray(usersData) ? usersData.length : usersData.count || 0
    }
    
    console.log('Stats loaded:', stats.value)
  } catch (error) {
    console.error('Error loading stats:', error)
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  if (authStore.isAdmin) {
    await loadStats()
  } else {
    await loadMahasiswaData()
  }
})
</script>

<style scoped>
.dashboard-wrapper {
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

.dashboard-container {
  flex: 1;
  margin-left: 280px;
  padding: 2rem;
  max-width: calc(100% - 280px);
}

.dashboard-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 20px;
  padding: 2.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
}

.greeting h1 {
  font-size: 2rem;
  margin: 0 0 0.5rem 0;
  font-weight: 700;
}

.greeting p {
  margin: 0;
  opacity: 0.9;
  font-size: 1.125rem;
}

.role-badge {
  display: inline-block;
  background: rgba(255, 255, 255, 0.2);
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: capitalize;
}

.header-actions {
  display: flex;
  gap: 1rem;
}

.date-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.15);
  padding: 0.75rem 1.25rem;
  border-radius: 12px;
  backdrop-filter: blur(10px);
}

.dashboard-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.stat-card {
  background: white;
  border-radius: 16px;
  padding: 1.75rem;
  display: flex;
  gap: 1.25rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.stat-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #667eea, #764ba2);
  opacity: 0;
  transition: opacity 0.3s;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.stat-card:hover::before {
  opacity: 1;
}

.stat-card.loading {
  opacity: 0.6;
  pointer-events: none;
}

.stat-icon-wrapper {
  width: 64px;
  height: 64px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.gradient-blue {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.gradient-purple {
  background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
}

.gradient-green {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
}

.gradient-orange {
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
}

.stat-content {
  flex: 1;
}

.stat-label {
  color: #6b7280;
  font-size: 0.875rem;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.25rem;
}

.stat-change {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.875rem;
  color: #6b7280;
}

.stat-change.positive {
  color: #10b981;
}

.section-header {
  margin-bottom: 1.5rem;
}

.section-header h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
}

.section-header p {
  color: #6b7280;
  margin: 0;
  font-size: 0.95rem;
}

.action-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
}

.action-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  text-decoration: none;
  color: inherit;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.action-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  opacity: 0;
  transition: opacity 0.3s;
}

.action-card:hover {
  transform: translateX(5px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.action-card:hover::before {
  opacity: 1;
}

.action-icon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.action-content {
  flex: 1;
}

.action-content h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
}

.action-content p {
  color: #6b7280;
  margin: 0;
  font-size: 0.875rem;
}

.action-arrow {
  font-size: 1.5rem;
  color: #9ca3af;
  transition: transform 0.3s;
}

.action-card:hover .action-arrow {
  transform: translateX(5px);
  color: #667eea;
}

.recent-activity {
  margin-top: 1rem;
}

.activity-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.activity-items {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  border-radius: 12px;
  background: #f9fafb;
  transition: background 0.3s;
}

.activity-item:hover {
  background: #f3f4f6;
}

.activity-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.activity-icon.success {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
}

.activity-icon.info {
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
}

.activity-content {
  flex: 1;
}

.activity-content h4 {
  font-size: 1rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
}

.activity-content p {
  color: #6b7280;
  margin: 0;
  font-size: 0.875rem;
}

.activity-time {
  color: #10b981;
  font-size: 0.875rem;
  font-weight: 600;
  background: rgba(16, 185, 129, 0.1);
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
}

@media (max-width: 1024px) {
  .sidebar {
    transform: translateX(-100%);
    transition: transform 0.3s;
  }

  .sidebar.open {
    transform: translateX(0);
  }

  .dashboard-container {
    margin-left: 0;
    max-width: 100%;
  }
}

@media (max-width: 768px) {
  .dashboard-container {
    padding: 1rem;
  }

  .dashboard-header {
    padding: 1.5rem;
  }

  .header-content {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .greeting h1 {
    font-size: 1.5rem;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .action-cards {
    grid-template-columns: 1fr;
  }
}

/* Mahasiswa Dashboard Styles */
.mahasiswa-profile-card {
  background: white;
  border-radius: 20px;
  padding: 2.5rem;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
}

.profile-header-section {
  display: flex;
  align-items: center;
  gap: 2rem;
  padding-bottom: 2rem;
  border-bottom: 2px solid #e5e7eb;
  margin-bottom: 2rem;
}

.large-avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3.5rem;
  font-weight: bold;
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
}

.profile-info-section h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
}

.nim-text {
  font-size: 1.125rem;
  color: #6b7280;
  margin: 0.25rem 0;
  font-weight: 600;
}

.prodi-text {
  font-size: 1rem;
  color: #667eea;
  margin: 0.25rem 0;
  font-weight: 500;
}

.profile-details-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.detail-box {
  background: #f9fafb;
  border-radius: 12px;
  padding: 1.5rem;
  display: flex;
  gap: 1rem;
  border: 1px solid #e5e7eb;
  transition: all 0.3s;
}

.detail-box:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.detail-box.full-width {
  grid-column: 1 / -1;
}

.detail-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.detail-content {
  flex: 1;
}

.detail-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #6b7280;
  margin-bottom: 0.25rem;
}

.detail-value {
  font-size: 1rem;
  color: #1f2937;
  font-weight: 500;
}

.action-buttons {
  display: flex;
  justify-content: center;
  padding-top: 2rem;
  border-top: 2px solid #e5e7eb;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 2rem;
  border-radius: 12px;
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

@media (max-width: 768px) {
  .mahasiswa-profile-card {
    padding: 1.5rem;
  }

  .profile-header-section {
    flex-direction: column;
    text-align: center;
  }

  .profile-details-grid {
    grid-template-columns: 1fr;
  }

  .large-avatar {
    width: 100px;
    height: 100px;
    font-size: 3rem;
  }

  .profile-info-section h2 {
    font-size: 1.5rem;
  }
}
</style>
