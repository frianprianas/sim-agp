# SIM AGP - Sistem Informasi Mahasiswa

## Project Overview
Aplikasi web pengelolaan mahasiswa menggunakan:
- **Backend**: Django 4.2 + Django REST Framework
- **Frontend**: Vue.js 3 + Vite
- **Database**: PostgreSQL (Production) / SQLite (Development)

## Struktur Project
```
sim-agp/
├── config/              # Django configuration
├── core/                # Main Django app (models, views, serializers)
├── database/            # SQL files (MySQL → PostgreSQL conversion)
├── frontend/            # Vue.js application
│   ├── src/
│   │   ├── components/  # Reusable Vue components
│   │   ├── views/       # Page components
│   │   ├── router/      # Vue Router
│   │   ├── stores/      # Pinia state management
│   │   └── services/    # API service layer
│   └── package.json
├── templates/           # Django templates
├── static/              # Static files
└── manage.py
```

## Database Models
- **Prodi**: Program Studi (id_prodi, prodi, jenjang)
- **Mahasiswa**: Data mahasiswa (nim, nama, alamat, dll)
- **User**: Custom user model dengan role (admin/mahasiswa)

## API Endpoints
- `/api/auth/` - Authentication (login, register, logout, profile)
- `/api/prodi/` - Program Studi CRUD
- `/api/mahasiswa/` - Mahasiswa CRUD
- `/api/users/` - User management

## Development Status
✅ Database conversion MySQL → PostgreSQL completed
✅ Django models created
✅ Django REST API configured
✅ Vue.js frontend scaffolded
✅ Authentication & authorization setup
✅ State management with Pinia
✅ API service layer created
✅ Vue Router configured
✅ Basic components & views created

## Next Steps
- Test authentication flow
- Complete CRUD operations in Vue.js
- Add form validation
- Enhance UI/UX
- Add error handling
- Implement loading states

## Development Commands

### Backend
```bash
venv\Scripts\activate
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm run dev
```

## Important Notes
- Custom User model: AUTH_USER_MODEL = 'core.User'
- Token authentication configured
- CORS enabled for frontend (port 5173)
- PostgreSQL conversion file: `database/sima_agp_postgresql.sql`
