<template>
  <div class="login-page">
    <div class="login-container">
      <div class="card login-card">
        <h1>🎓 SIM AGP</h1>
        <h2>Register</h2>
        
        <div v-if="error" class="alert alert-danger">
          {{ error }}
        </div>

        <form @submit.prevent="handleRegister">
          <div class="form-group">
            <label for="name">Nama Lengkap</label>
            <input
              id="name"
              v-model="form.name"
              type="text"
              class="form-control"
              required
            />
          </div>

          <div class="form-group">
            <label for="username">Username</label>
            <input
              id="username"
              v-model="form.username"
              type="text"
              class="form-control"
              required
            />
          </div>

          <div class="form-group">
            <label for="email">Email</label>
            <input
              id="email"
              v-model="form.email"
              type="email"
              class="form-control"
            />
          </div>

          <div class="form-group">
            <label for="password">Password</label>
            <input
              id="password"
              v-model="form.password"
              type="password"
              class="form-control"
              required
              minlength="6"
            />
          </div>

          <div class="form-group">
            <label for="password_confirmation">Konfirmasi Password</label>
            <input
              id="password_confirmation"
              v-model="form.password_confirmation"
              type="password"
              class="form-control"
              required
            />
          </div>

          <button type="submit" class="btn btn-primary btn-block" :disabled="loading">
            {{ loading ? 'Loading...' : 'Register' }}
          </button>
        </form>

        <p class="text-center mt-3">
          Sudah punya akun? <router-link to="/login">Login disini</router-link>
        </p>
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
  name: '',
  username: '',
  email: '',
  password: '',
  password_confirmation: '',
  role: 'mahasiswa',
})

const loading = ref(false)
const error = ref('')

const handleRegister = async () => {
  loading.value = true
  error.value = ''

  try {
    await authStore.register(form.value)
    router.push('/dashboard')
  } catch (err) {
    error.value = err.response?.data?.error || 'Registrasi gagal. Silakan coba lagi.'
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
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
}

.login-container {
  width: 100%;
  max-width: 450px;
  padding: 1rem;
}

.login-card {
  text-align: center;
}

.login-card h1 {
  color: var(--primary-color);
  margin-bottom: 0.5rem;
}

.login-card h2 {
  margin-bottom: 1.5rem;
  color: #374151;
}

.form-group {
  text-align: left;
}

.btn-block {
  width: 100%;
  margin-top: 1rem;
}

.text-center {
  text-align: center;
}

.mt-3 {
  margin-top: 1rem;
}
</style>
