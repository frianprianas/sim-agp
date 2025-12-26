<template>
  <div>
    <Navbar />
    <div class="container">
      <div class="prodi-list">
        <h1>Program Studi</h1>

        <div v-if="loading" class="spinner"></div>

        <div v-else-if="error" class="alert alert-danger">{{ error }}</div>

        <div v-else>
          <div class="prodi-grid">
            <div v-for="p in prodi" :key="p.id_prodi" class="card prodi-card">
              <h3>{{ p.prodi }}</h3>
              <p class="jenjang">{{ p.jenjang === 'D3' ? 'Diploma 3' : 'Sarjana' }}</p>
              <p class="meta">ID: {{ p.id_prodi }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { prodiService } from '@/services'
import Navbar from '@/components/Navbar.vue'

const prodi = ref([])
const loading = ref(true)
const error = ref('')

const fetchProdi = async () => {
  try {
    loading.value = true
    const data = await prodiService.getAll()
    prodi.value = data.results || data
  } catch (err) {
    error.value = 'Gagal memuat data program studi'
    console.error(err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchProdi()
})
</script>

<style scoped>
.prodi-list {
  max-width: 1200px;
  margin: 0 auto;
}

.prodi-list h1 {
  color: var(--primary-color);
  margin-bottom: 1.5rem;
}

.prodi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.prodi-card {
  padding: 2rem;
  text-align: center;
  transition: transform 0.3s;
}

.prodi-card:hover {
  transform: translateY(-5px);
}

.prodi-card h3 {
  color: var(--primary-color);
  margin-bottom: 0.5rem;
}

.jenjang {
  font-size: 1.125rem;
  color: #6b7280;
  margin-bottom: 1rem;
}

.meta {
  font-size: 0.875rem;
  color: #9ca3af;
}
</style>
