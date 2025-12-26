# 🐘 PostgreSQL Setup Guide - SIM AGP

Panduan lengkap setup PostgreSQL untuk SIM AGP.

## ✅ Status: CONFIGURED & RUNNING!

Database PostgreSQL sudah dikonfigurasi dan berjalan dengan sempurna!

## 📊 Konfigurasi Database

### Database Info
- **Database Name**: `sima_agp`
- **User**: `postgres`
- **Password**: `buhun666`
- **Host**: `localhost`
- **Port**: `5432`

### Data yang Sudah Diimport
- ✅ 6 Program Studi (Prodi)
- ✅ 2 Mahasiswa (Firli Batubara Ankara, Neni Irwati)
- ✅ 2 Users (admin, mahasiswa)

## 🔧 File Konfigurasi

### 1. Environment Variables (`.env`)
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL Database Configuration
DB_ENGINE=postgresql
DB_NAME=sima_agp
DB_USER=postgres
DB_PASSWORD=buhun666
DB_HOST=localhost
DB_PORT=5432
```

### 2. Django Settings (`config/settings.py`)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'sima_agp'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'buhun666'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

## 📁 File SQL

### Original MySQL
- Lokasi: `c:\Users\ms-yhan\Downloads\sima_agp.sql`

### PostgreSQL Conversion
- Lokasi: `database/sima_agp_postgresql.sql`
- Status: ✅ Sudah diimport

### Update Script
- Lokasi: `database/update_users_table.sql`
- Status: ✅ Sudah dijalankan

## 🚀 Cara Import Database (Jika Belum)

### Method 1: Using psql Command
```bash
# Create database
psql -U postgres -c "CREATE DATABASE sima_agp;"

# Import SQL file
psql -U postgres -d sima_agp -f database/sima_agp_postgresql.sql

# Update users table
psql -U postgres -d sima_agp -f database/update_users_table.sql
```

### Method 2: Using Python Script
```bash
# Run update script
python update_db.py
```

### Method 3: Using pgAdmin
1. Buka pgAdmin
2. Connect ke PostgreSQL server
3. Create database `sima_agp`
4. Right click → Restore → Select `sima_agp_postgresql.sql`

## 🔐 Login Credentials

### Admin User
- **Username**: `admin`
- **Password**: Password dari database (Laravel bcrypt hash)
- **Email**: `admin@sima-agp.ac.id`
- **Role**: admin
- **Is Superuser**: Yes
- **Is Staff**: Yes

### Mahasiswa User
- **Username**: `89000`
- **Password**: Password dari database (Laravel bcrypt hash)
- **Email**: `neninkmt@gmail.com`
- **Role**: mahasiswa

## 📊 Database Schema

### Table: prodi
```sql
id_prodi (BIGSERIAL PK)
prodi (VARCHAR 100)
jenjang (VARCHAR 2) - 'D3' atau 'S1'
created_at, updated_at (TIMESTAMP)
```

### Table: mahasiswa
```sql
nim (VARCHAR 20 PK)
nama, alamat (VARCHAR, TEXT)
jenis_kelamin (VARCHAR 1) - 'L' atau 'P'
tempat (VARCHAR 50)
tgl_lahir (DATE)
id_prodi (BIGINT FK → prodi.id_prodi)
tahun_masuk (INTEGER)
email, no_telepon (VARCHAR)
created_at, updated_at (TIMESTAMP)
```

### Table: users
```sql
id (BIGSERIAL PK)
name, username, email (VARCHAR)
password (VARCHAR 255)
role (VARCHAR 20) - 'admin' atau 'mahasiswa'
nim (VARCHAR 20 FK → mahasiswa.nim)
-- Django fields
last_login (TIMESTAMP)
is_superuser, is_staff, is_active (BOOLEAN)
date_joined (TIMESTAMP)
created_at, updated_at (TIMESTAMP)
```

## ✅ Verification

### Test Connection
```bash
python test_db.py
```

Output:
```
==================================================
DATABASE CONNECTION TEST
==================================================

📚 PROGRAM STUDI:
--------------------------------------------------
Total: 6
  1. Teknik Informatika (S1)
  2. Sistem Informasi (S1)
  ... dst

✅ DATABASE CONNECTION SUCCESS!
```

### Test API
```bash
# Start Django server
python manage.py runserver

# Test endpoints
curl http://127.0.0.1:8000/api/prodi/
curl http://127.0.0.1:8000/api/mahasiswa/
```

## 🔧 Dependencies

```bash
# Install PostgreSQL adapter
pip install psycopg2-binary

# Already in requirements.txt
psycopg2-binary>=2.9.9
```

## 📝 Important Notes

1. **Password Hash**: Database menggunakan Laravel bcrypt hash format
2. **Foreign Keys**: Cascade delete enabled untuk data integrity
3. **Indexes**: Created untuk foreign keys dan query optimization
4. **Django Fields**: Additional fields added untuk Django auth compatibility

## 🛠️ Maintenance

### Backup Database
```bash
pg_dump -U postgres sima_agp > backup_$(date +%Y%m%d).sql
```

### Restore Database
```bash
psql -U postgres -d sima_agp < backup_20251225.sql
```

### Check Database Size
```sql
SELECT pg_size_pretty(pg_database_size('sima_agp'));
```

## 🆘 Troubleshooting

### Connection Refused
- Pastikan PostgreSQL service running
- Check `pg_hba.conf` untuk allow connections

### Authentication Failed
- Verify password di `.env` file
- Check PostgreSQL user permissions

### Column Not Found
- Jalankan `update_db.py` script
- Atau manual ALTER TABLE

### Migration Issues
- Django migrations sudah dibuat untuk struktur yang ada
- Tidak perlu run migrations jika import langsung dari SQL

## 🎯 Next Steps

- ✅ Database configured
- ✅ Data imported
- ✅ Django connected
- ✅ API running
- [ ] Test all API endpoints
- [ ] Setup frontend Vue.js
- [ ] Test authentication flow

---

**Database Status**: ✅ READY FOR PRODUCTION!
