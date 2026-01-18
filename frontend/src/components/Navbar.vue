<template>
  <nav class="navbar">
    <div class="container navbar-content">
      <div class="navbar-brand">
        <h2>🎓 SIM AGP</h2>
      </div>
      <div class="navbar-menu">
        <router-link to="/dashboard" class="nav-link">Dashboard</router-link>
        <template v-if="authStore.isAdmin">
          <router-link to="/mahasiswa" class="nav-link">Mahasiswa</router-link>
          <router-link to="/prodi" class="nav-link">Program Studi</router-link>
          <router-link to="/profile" class="nav-link">Profile</router-link>
        </template>
        <template v-else>
          <router-link to="/profile" class="nav-link">Ubah Email & Password</router-link>
        </template>
        <router-link to="/settings" class="nav-link">Pengaturan</router-link>
        <button @click="handleLogout" class="btn btn-danger btn-sm">Logout</button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const handleLogout = async () => {
  try {
    await authStore.logout()
    router.push('/login')
  } catch (error) {
    console.error('Logout error:', error)
  }
}
</script>

<style scoped>
.navbar {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  padding: 1rem 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.navbar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar-brand h2 {
  color: white;
  margin: 0;
}

.navbar-menu {
  display: flex;
  gap: 1.5rem;
  align-items: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-weight: 500;
  transition: opacity 0.3s;
}

.nav-link:hover,
.nav-link.router-link-active {
  opacity: 0.8;
}

.btn-sm {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
}
</style>
