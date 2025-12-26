<template>
  <div class="login-page">
    <div class="login-container">
      <div class="login-left">
        <div class="branding">
          <div class="logo-container">
            <div class="logo-circle">
              <svg width="80" height="80" viewBox="0 0 80 80" fill="none">
                <path d="M40 10L15 25V55L40 70L65 55V25L40 10Z" fill="url(#gradient1)" stroke="#fff" stroke-width="2"/>
                <path d="M40 25L30 30V50L40 55L50 50V30L40 25Z" fill="#fff" opacity="0.3"/>
                <defs>
                  <linearGradient id="gradient1" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#667eea" />
                    <stop offset="100%" style="stop-color:#764ba2" />
                  </linearGradient>
                </defs>
              </svg>
            </div>
          </div>
          <h1>SIM AGP</h1>
          <p class="subtitle">Sistem Informasi Mahasiswa</p>
          <div class="features">
            <div class="feature-item">
              <span class="icon">✓</span>
              <span>Manajemen Data Mahasiswa</span>
            </div>
            <div class="feature-item">
              <span class="icon">✓</span>
              <span>Program Studi Terintegrasi</span>
            </div>
            <div class="feature-item">
              <span class="icon">✓</span>
              <span>Dashboard Interaktif</span>
            </div>
            <div class="feature-item">
              <span class="icon">✓</span>
              <span>Keamanan Terjamin</span>
            </div>
          </div>
        </div>
      </div>

      <div class="login-right">
        <div class="login-card">
          <div class="card-header">
            <h2>Selamat Datang</h2>
            <p>Silakan login untuk melanjutkan</p>
          </div>

          <div v-if="error" class="alert alert-danger">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"/>
            </svg>
            {{ error }}
          </div>

          <form @submit.prevent="handleLogin" class="login-form">
            <div class="form-group">
              <label for="username">
                <svg width="18" height="18" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"/>
                </svg>
                Username
              </label>
              <input
                id="username"
                v-model="form.username"
                type="text"
                class="form-control"
                placeholder="Masukkan username anda"
                required
                :disabled="loading"
              />
            </div>

            <div class="form-group">
              <label for="password">
                <svg width="18" height="18" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"/>
                </svg>
                Password
              </label>
              <input
                id="password"
                v-model="form.password"
                type="password"
                class="form-control"
                placeholder="Masukkan password anda"
                required
                :disabled="loading"
              />
            </div>

            <button type="submit" class="btn btn-primary btn-block" :disabled="loading">
              <span v-if="loading" class="loading-spinner"></span>
              <span v-else>
                <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M3 3a1 1 0 011 1v12a1 1 0 11-2 0V4a1 1 0 011-1zm7.707 3.293a1 1 0 010 1.414L9.414 9H17a1 1 0 110 2H9.414l1.293 1.293a1 1 0 01-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0z"/>
                </svg>
                Login
              </span>
            </button>
          </form>

          <div class="divider">
            <span>atau</span>
          </div>

          <p class="register-link">
            Belum punya akun? 
            <router-link to="/register">Daftar sekarang</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const form = ref({
  username: '',
  password: '',
})

const loading = ref(false)
const error = ref('')

const handleLogin = async () => {
  loading.value = true
  error.value = ''

  try {
    await authStore.login(form.value.username, form.value.password)
    router.push('/dashboard')
  } catch (err) {
    error.value = err.response?.data?.error || 'Login gagal. Silakan coba lagi.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  position: relative;
  overflow: hidden;
}

.login-page::before {
  content: '';
  position: absolute;
  width: 500px;
  height: 500px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  top: -250px;
  left: -250px;
}

.login-page::after {
  content: '';
  position: absolute;
  width: 400px;
  height: 400px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  bottom: -200px;
  right: -200px;
}

.login-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  max-width: 1000px;
  width: 100%;
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  position: relative;
  z-index: 1;
  margin: 2rem;
}

.login-left {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 3rem;
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.branding {
  text-align: center;
}

.logo-container {
  margin-bottom: 2rem;
}

.logo-circle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

.branding h1 {
  font-size: 2.5rem;
  margin: 0 0 0.5rem 0;
  font-weight: 700;
  text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.subtitle {
  font-size: 1.125rem;
  margin-bottom: 3rem;
  opacity: 0.9;
}

.features {
  text-align: left;
  margin-top: 2rem;
}

.feature-item {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
  font-size: 0.95rem;
}

.feature-item .icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  margin-right: 0.75rem;
  font-weight: bold;
}

.login-right {
  padding: 3rem;
  display: flex;
  align-items: center;
}

.login-card {
  width: 100%;
}

.card-header {
  margin-bottom: 2rem;
}

.card-header h2 {
  font-size: 1.875rem;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
  font-weight: 700;
}

.card-header p {
  color: #6b7280;
  margin: 0;
  font-size: 0.95rem;
}

.alert {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
}

.alert svg {
  flex-shrink: 0;
}

.login-form {
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
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

.btn-primary {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.875rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  border-radius: 10px;
  color: white;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  margin-top: 0.5rem;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
}

.btn-primary:disabled {
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

.divider {
  position: relative;
  text-align: center;
  margin: 1.5rem 0;
}

.divider::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 1px;
  background: #e5e7eb;
}

.divider span {
  position: relative;
  background: white;
  padding: 0 1rem;
  color: #9ca3af;
  font-size: 0.875rem;
}

.register-link {
  text-align: center;
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0;
}

.register-link a {
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s;
}

.register-link a:hover {
  color: #764ba2;
  text-decoration: underline;
}

@media (max-width: 768px) {
  .login-container {
    grid-template-columns: 1fr;
    margin: 1rem;
  }

  .login-left {
    display: none;
  }

  .login-right {
    padding: 2rem 1.5rem;
  }
}
</style>
