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

          <router-link to="/settings" class="nav-item" exact-active-class="active">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"/>
            </svg>
            <span>Pengaturan</span>
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
            <h1>⚙️ Pengaturan</h1>
            <p>Kelola preferensi aplikasi Anda</p>
          </div>

          <div class="settings-grid">
            <!-- Appearance Settings -->
            <div class="settings-card">
              <div class="settings-card-header">
                <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"/>
                </svg>
                <h3>Tampilan</h3>
              </div>
              
              <div class="settings-card-body">
                <div class="setting-item">
                  <div class="setting-info">
                    <div class="setting-label">Dark Mode</div>
                    <div class="setting-description">Gunakan tema gelap untuk mengurangi kelelahan mata</div>
                  </div>
                  <label class="toggle-switch">
                    <input type="checkbox" v-model="darkMode" @change="toggleDarkMode">
                    <span class="toggle-slider"></span>
                  </label>
                </div>
              </div>
            </div>

            <!-- User Info Settings -->
            <div class="settings-card">
              <div class="settings-card-header">
                <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"/>
                </svg>
                <h3>Informasi Akun</h3>
              </div>
              
              <div class="settings-card-body">
                <div class="info-item">
                  <span class="info-label">Username:</span>
                  <span class="info-value">{{ authStore.user?.username }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">Email:</span>
                  <span class="info-value">{{ authStore.user?.email || '-' }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">Role:</span>
                  <span class="info-value role-badge">{{ authStore.user?.role }}</span>
                </div>
              </div>
            </div>

            <!-- About Settings -->
            <div class="settings-card">
              <div class="settings-card-header">
                <svg width="24" height="24" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
                </svg>
                <h3>Tentang Aplikasi</h3>
              </div>
              
              <div class="settings-card-body">
                <div class="info-item">
                  <span class="info-label">Aplikasi:</span>
                  <span class="info-value">SIM AGP</span>
                </div>
                <div class="info-item">
                  <span class="info-label">Versi:</span>
                  <span class="info-value">1.0.0</span>
                </div>
                <div class="info-item">
                  <span class="info-label">Teknologi:</span>
                  <span class="info-value">Django + Vue.js</span>
                </div>
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
import { useAuthStore } from '@/stores/auth'
import Navbar from '@/components/Navbar.vue'

const authStore = useAuthStore()
const darkMode = ref(false)

const toggleDarkMode = () => {
  if (darkMode.value) {
    document.body.classList.add('dark-mode')
    document.documentElement.classList.add('dark-mode')
    localStorage.setItem('darkMode', 'true')
  } else {
    document.body.classList.remove('dark-mode')
    document.documentElement.classList.remove('dark-mode')
    localStorage.setItem('darkMode', 'false')
  }
}

onMounted(() => {
  // Load dark mode preference
  const savedDarkMode = localStorage.getItem('darkMode')
  if (savedDarkMode === 'true') {
    darkMode.value = true
    document.body.classList.add('dark-mode')
    document.documentElement.classList.add('dark-mode')
  }
})
</script>

<style scoped>
.page-wrapper {
  min-height: 100vh;
  background: var(--bg-color);
}

.dashboard-layout {
  display: flex;
}

.sidebar {
  width: 260px;
  background: white;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  z-index: 100;
}

.sidebar-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.logo span {
  font-size: 1.25rem;
  font-weight: 700;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.sidebar-nav {
  flex: 1;
  padding: 1rem;
  overflow-y: auto;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.875rem 1rem;
  border-radius: 10px;
  color: #6b7280;
  text-decoration: none;
  transition: all 0.3s;
  margin-bottom: 0.5rem;
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
  padding: 1rem;
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
  font-weight: 600;
  font-size: 1rem;
}

.user-details {
  flex: 1;
}

.user-name {
  font-weight: 600;
  color: #1f2937;
  font-size: 0.875rem;
}

.user-role {
  font-size: 0.75rem;
  color: #6b7280;
  text-transform: capitalize;
}

.main-content {
  margin-left: 260px;
  flex: 1;
  padding: 2rem;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
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

.settings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
}

.settings-card {
  background: white;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  overflow: hidden;
  transition: all 0.3s;
}

.settings-card:hover {
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.settings-card-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.settings-card-header h3 {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 600;
}

.settings-card-body {
  padding: 1.5rem;
}

.setting-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.setting-info {
  flex: 1;
}

.setting-label {
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}

.setting-description {
  font-size: 0.875rem;
  color: #6b7280;
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 52px;
  height: 28px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #cbd5e1;
  transition: 0.3s;
  border-radius: 28px;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 20px;
  width: 20px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: 0.3s;
  border-radius: 50%;
}

input:checked + .toggle-slider {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

input:checked + .toggle-slider:before {
  transform: translateX(24px);
}

.info-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.875rem 0;
  border-bottom: 1px solid #f3f4f6;
}

.info-item:last-child {
  border-bottom: none;
}

.info-label {
  font-weight: 600;
  color: #6b7280;
  font-size: 0.875rem;
}

.info-value {
  font-weight: 500;
  color: #1f2937;
}

.role-badge {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 600;
  text-transform: capitalize;
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

  .settings-grid {
    grid-template-columns: 1fr;
  }
}

/* Dark Mode Styles */
:global(.dark-mode) .sidebar {
  background: #1f2937;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.3);
}

:global(.dark-mode) .sidebar-header {
  border-bottom-color: #374151;
}

:global(.dark-mode) .nav-item {
  color: #9ca3af;
}

:global(.dark-mode) .nav-item:hover {
  background: #374151;
  color: #667eea;
}

:global(.dark-mode) .nav-divider {
  background: #374151;
}

:global(.dark-mode) .sidebar-footer {
  border-top-color: #374151;
}

:global(.dark-mode) .user-name {
  color: #f3f4f6;
}

:global(.dark-mode) .user-role {
  color: #9ca3af;
}

:global(.dark-mode) .main-content {
  background: #111827;
}

:global(.dark-mode) .page-header h1 {
  color: #f3f4f6;
}

:global(.dark-mode) .page-header p {
  color: #9ca3af;
}

:global(.dark-mode) .settings-card {
  background: #1f2937;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

:global(.dark-mode) .settings-card:hover {
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
}

:global(.dark-mode) .settings-card-body {
  background: #1f2937;
}

:global(.dark-mode) .setting-label {
  color: #f3f4f6;
}

:global(.dark-mode) .setting-description {
  color: #9ca3af;
}

:global(.dark-mode) .info-item {
  border-bottom-color: #374151;
}

:global(.dark-mode) .info-label {
  color: #9ca3af;
}

:global(.dark-mode) .info-value {
  color: #f3f4f6;
}
</style>
