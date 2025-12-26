# SIM AGP Frontend

Frontend Vue.js untuk Sistem Informasi Mahasiswa AGP.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build
```

## 📁 Struktur Project

```
frontend/
├── src/
│   ├── components/        # Reusable components
│   │   └── Navbar.vue
│   ├── views/            # Page components
│   │   ├── Login.vue
│   │   ├── Register.vue
│   │   ├── Dashboard.vue
│   │   ├── Profile.vue
│   │   ├── mahasiswa/
│   │   │   ├── List.vue
│   │   │   ├── Form.vue
│   │   │   └── Detail.vue
│   │   └── prodi/
│   │       └── List.vue
│   ├── router/           # Vue Router configuration
│   │   └── index.js
│   ├── stores/           # Pinia stores
│   │   └── auth.js
│   ├── services/         # API services
│   │   ├── api.js
│   │   └── index.js
│   ├── App.vue          # Root component
│   ├── main.js          # Entry point
│   └── style.css        # Global styles
├── index.html           # HTML template
├── vite.config.js       # Vite configuration
└── package.json         # Dependencies
```

## 🔧 Configuration

Backend API URL dikonfigurasi di `src/services/api.js`:
```javascript
baseURL: 'http://localhost:8000'
```

## 🎨 Features

- Vue 3 Composition API
- Vue Router untuk routing
- Pinia untuk state management
- Axios untuk HTTP requests
- Token-based authentication
- Role-based access control

## 📝 Development

Server development akan berjalan di `http://localhost:5173` dengan hot-reload.

## 🏗️ Build

```bash
npm run build
```

File production akan ada di folder `dist/`.
