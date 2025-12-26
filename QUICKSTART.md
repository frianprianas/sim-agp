# 🚀 Quick Start Guide - SIM AGP

Panduan cepat untuk menjalankan aplikasi SIM AGP.

## ⚡ Quick Setup (5 Menit)

### 1. Backend Django
```bash
# Aktivasi virtual environment
venv\Scripts\activate

# Install dependencies (jika belum)
pip install -r requirements.txt

# Setup database
python manage.py migrate

# Buat superuser
python manage.py createsuperuser

# Jalankan server
python manage.py runserver
```
✅ Backend berjalan di: http://127.0.0.1:8000

### 2. Frontend Vue.js
```bash
# Masuk ke folder frontend
cd frontend

# Install dependencies
npm install

# Jalankan dev server
npm run dev
```
✅ Frontend berjalan di: http://localhost:5173

## 🎯 Testing

1. Buka browser ke: http://localhost:5173
2. Login dengan kredensial yang dibuat
3. Explore dashboard dan fitur aplikasi

## 📊 Import Data PostgreSQL (Opsional)

Jika ingin menggunakan data dari MySQL yang sudah dikonversi:

```bash
# Masuk ke PostgreSQL
psql -U postgres

# Buat database
CREATE DATABASE sima_agp;

# Keluar dan import
\q

# Import file SQL
psql -U postgres -d sima_agp -f database/sima_agp_postgresql.sql
```

## 🔧 Update Django Settings untuk PostgreSQL

Edit `config/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sima_agp',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Atau gunakan environment variable di `.env`:
```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/sima_agp
```

## ✅ Checklist

- [ ] Python 3.8+ terinstall
- [ ] Node.js 16+ terinstall
- [ ] Virtual environment dibuat dan diaktifkan
- [ ] Dependencies backend terinstall
- [ ] Database migrations dijalankan
- [ ] Superuser dibuat
- [ ] Dependencies frontend terinstall
- [ ] Backend server berjalan di port 8000
- [ ] Frontend server berjalan di port 5173

## 🆘 Troubleshooting

### Backend tidak bisa diakses
- Pastikan virtual environment sudah diaktifkan
- Check port 8000 tidak digunakan aplikasi lain

### Frontend tidak bisa connect ke backend
- Pastikan backend berjalan di port 8000
- Check CORS settings di Django

### Error saat migration
- Pastikan database settings benar
- Untuk PostgreSQL, pastikan service berjalan

## 📚 Resources

- Backend API Docs: http://127.0.0.1:8000/api/
- Django Admin: http://127.0.0.1:8000/admin/
- Frontend App: http://localhost:5173

---

**Happy Coding! 🎓**
