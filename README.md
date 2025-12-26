# SIM AGP - Sistem Informasi Mahasiswa

Aplikasi web untuk pengelolaan data mahasiswa menggunakan **Django (Backend)** dan **Vue.js (Frontend)**.

## 📋 Daftar Isi

- [Fitur](#-fitur)
- [Teknologi](#-teknologi)
- [Instalasi](#-instalasi)
- [Struktur Database](#-struktur-database)
- [API Endpoints](#-api-endpoints)
- [Penggunaan](#-penggunaan)

## ✨ Fitur

- **Autentikasi & Otorisasi**
  - Login dan Register
  - Role-based access (Admin & Mahasiswa)
  - Token-based authentication

- **Dashboard Role-Based**
  - **Admin Dashboard**: Statistik lengkap (total mahasiswa, prodi, users)
  - **Mahasiswa Dashboard**: Menampilkan hanya data diri sendiri

- **Manajemen Mahasiswa (Admin)**
  - CRUD data mahasiswa
  - Set/ubah password mahasiswa
  - Filter berdasarkan prodi dan tahun masuk
  - Detail mahasiswa lengkap

- **Profile Mahasiswa**
  - Lihat data diri lengkap
  - Ubah email sendiri
  - Ubah password sendiri

- **Manajemen Program Studi (Admin)**
  - Tambah dan ubah program studi
  - Filter berdasarkan jenjang (D3/D4/S1/S2/S3)

- **Universal Sidebar Navigation**
  - Sidebar konsisten di semua halaman
  - Menu navigasi berdasarkan role

## 🛠 Teknologi

### Backend
- Python 3.8+
- Django 4.2
- Django REST Framework
- PostgreSQL (Production) / SQLite (Development)

### Frontend
- Vue.js 3
- Vite
- Pinia (State Management)
- Vue Router
- Axios

## 🚀 Instalasi

### Prerequisites
- Python 3.8 atau lebih tinggi
- Node.js 16 atau lebih tinggi
- PostgreSQL (untuk production)

### Backend Setup

1. **Clone repository dan masuk ke direktori project**
   ```bash
   cd sim-agp
   ```

2. **Buat virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Aktifkan virtual environment**
   
   Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Setup environment variables**
   
   Copy file `.env.example` menjadi `.env`:
   ```bash
   copy .env.example .env
   ```
   
   Edit `.env` dan sesuaikan konfigurasi database:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   
   # PostgreSQL (Production)
   DATABASE_URL=postgresql://user:password@localhost:5432/sima_agp
   
   # SQLite (Development) - default
   DATABASE_URL=sqlite:///db.sqlite3
   ```

6. **Jalankan migrasi database**
   ```bash
   python manage.py migrate
   ```

7. **Buat superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Jalankan development server**
   ```bash
   python manage.py runserver
   ```
   
   Backend akan berjalan di `http://127.0.0.1:8000`

### Frontend Setup

1. **Masuk ke direktori frontend**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Jalankan development server**
   ```bash
   npm run dev
   ```
   
   Frontend akan berjalan di `http://localhost:5173`

## 📊 Struktur Database

### Tabel: prodi
```sql
- id_prodi (BIGSERIAL, PK)
- prodi (VARCHAR 100)
- jenjang (VARCHAR 2) - 'D3' atau 'S1'
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

### Tabel: mahasiswa
```sql
- nim (VARCHAR 20, PK)
- nama (VARCHAR 100)
- alamat (TEXT)
- jenis_kelamin (VARCHAR 1) - 'L' atau 'P'
- tempat (VARCHAR 50)
- tgl_lahir (DATE)
- id_prodi (BIGINT, FK → prodi.id_prodi)
- tahun_masuk (INTEGER)
- email (VARCHAR 255)
- no_telepon (VARCHAR 20)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

### Tabel: users
```sql
- id (BIGSERIAL, PK)
- name (VARCHAR 255)
- username (VARCHAR 255, UNIQUE)
- email (VARCHAR 255)
- password (VARCHAR 255)
- role (VARCHAR 20) - 'admin' atau 'mahasiswa'
- nim (VARCHAR 20, FK → mahasiswa.nim, UNIQUE)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

## 🔌 API Endpoints

### Authentication
```
POST   /api/auth/login/          # Login
POST   /api/auth/register/       # Register
POST   /api/auth/logout/         # Logout
GET    /api/auth/profile/        # Get user profile
```

### Authentication
```
POST   /api/auth/login/          # Login user
POST   /api/auth/register/       # Register user baru
POST   /api/auth/logout/         # Logout user
GET    /api/auth/profile/        # Get profile user saat ini
PUT    /api/auth/update-profile/ # Update email & password (mahasiswa)
```

### Mahasiswa
```
GET    /api/mahasiswa/           # List semua mahasiswa
POST   /api/mahasiswa/           # Create mahasiswa baru (dengan password)
GET    /api/mahasiswa/:nim/      # Detail mahasiswa
PUT    /api/mahasiswa/:nim/      # Update mahasiswa (dan password)
DELETE /api/mahasiswa/:nim/      # Delete mahasiswa

# Custom endpoints
GET    /api/mahasiswa/by_prodi/?id_prodi=1
GET    /api/mahasiswa/by_tahun/?tahun=2025
```

### Program Studi
```
GET    /api/prodi/               # List semua prodi
POST   /api/prodi/               # Create prodi baru
GET    /api/prodi/:id/           # Detail prodi
PUT    /api/prodi/:id/           # Update prodi
DELETE /api/prodi/:id/           # Delete prodi

# Custom endpoints
GET    /api/prodi/by_jenjang/?jenjang=S1
```

### Users
```
GET    /api/users/               # List semua users
GET    /api/users/:id/           # Detail user
PUT    /api/users/:id/           # Update user
DELETE /api/users/:id/           # Delete user

# Custom endpoints
GET    /api/users/by_role/?role=admin
```

## 📖 Penggunaan

### Login

#### Login sebagai Admin
1. Buka `http://localhost:5173/login`
2. Username: `admin`
3. Password: `admin123`
4. Dashboard akan menampilkan statistik lengkap

#### Login sebagai Mahasiswa
1. Buka `http://localhost:5173/login`
2. Username: NIM mahasiswa (contoh: `666555`)
3. Password: password yang diset oleh admin
4. Dashboard akan menampilkan data mahasiswa tersebut saja

### Dashboard

#### Admin Dashboard
- Statistik total mahasiswa, prodi, users, dan tahun akademik
- Akses penuh ke semua menu (Mahasiswa, Prodi, Users)
- Dapat melakukan CRUD pada semua data

#### Mahasiswa Dashboard
- Menampilkan profil mahasiswa lengkap (NIM, nama, email, prodi, dll)
- Avatar besar dan informasi detail
- Tombol untuk ubah email dan password
- Hanya dapat melihat dan mengedit data sendiri

### Manajemen Mahasiswa (Admin)
- **Create**: Tambah mahasiswa baru dengan set password awal
- **Read**: Lihat daftar dan detail mahasiswa
- **Update**: Edit data mahasiswa dan ubah password (opsional)
- **Delete**: Hapus data mahasiswa

### Profile Mahasiswa (Mahasiswa)
- Lihat data diri lengkap di dashboard
- Klik "Ubah Email & Password" atau menu "Profil"
- Update email dan/atau password
- Password minimal 6 karakter
- Validasi otomatis

**Catatan:** Lihat [MAHASISWA_DASHBOARD.md](MAHASISWA_DASHBOARD.md) untuk panduan lengkap fitur mahasiswa.

### Import Database PostgreSQL
```bash
# Masuk ke PostgreSQL
psql -U postgres

# Buat database
CREATE DATABASE sima_agp;

# Import SQL file
\c sima_agp
\i database/sima_agp_postgresql.sql
```

### Migrasi dari MySQL ke PostgreSQL
1. File SQL MySQL sudah dikonversi ke PostgreSQL
2. Lokasi: `database/sima_agp_postgresql.sql`
3. Jalankan script SQL untuk membuat tabel dan data

## 📁 Struktur Project

```
sim-agp/
├── config/                 # Konfigurasi Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                   # App Django utama
│   ├── models.py          # Database models
│   ├── views.py           # API views
│   ├── serializers.py     # DRF serializers
│   ├── admin.py           # Django admin
│   └── urls.py            # URL routing
├── database/              # SQL files
│   └── sima_agp_postgresql.sql
├── frontend/              # Vue.js frontend
│   ├── src/
│   │   ├── components/   # Vue components
│   │   ├── views/        # Page views
│   │   ├── router/       # Vue Router
│   │   ├── stores/       # Pinia stores
│   │   ├── services/     # API services
│   │   └── App.vue
│   ├── package.json
│   └── vite.config.js
├── templates/             # Django templates
├── static/                # Static files
├── manage.py
├── requirements.txt
└── README.md
```

## 🔐 Default Credentials

Setelah import database:
- **Admin**
  - Username: `admin`
  - Password: `admin` (dari hash database)

## 🚧 Development

### Backend
```bash
# Membuat migration baru
python manage.py makemigrations

# Menjalankan migration
python manage.py migrate

# Membuat superuser
python manage.py createsuperuser

# Menjalankan tests
python manage.py test
```

### Frontend
```bash
# Install dependencies
npm install

# Development server
npm run dev

# Build untuk production
npm run build

# Preview production build
npm run preview
```

## 📝 Catatan

- File SQL MySQL original ada di `c:\Users\ms-yhan\Downloads\sima_agp.sql`
- File SQL PostgreSQL hasil konversi ada di `database/sima_agp_postgresql.sql`
- Password di database menggunakan hash bcrypt dari Laravel
- Untuk production, gunakan PostgreSQL dan set `DEBUG=False`

## 🤝 Kontribusi

1. Fork repository
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 License

Project ini dibuat untuk tujuan pembelajaran.

---

**Selamat Menggunakan SIM AGP! 🎓**
