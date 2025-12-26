# Dashboard Mahasiswa - Panduan Penggunaan

## Fitur Role-Based Dashboard

Aplikasi sekarang memiliki 2 jenis dashboard berdasarkan role user:

### 1. Dashboard Admin
- Menampilkan statistik total (mahasiswa, prodi, users, tahun akademik)
- Akses penuh ke semua fitur CRUD
- Dapat mengelola password mahasiswa

**Login Admin:**
- Username: `admin`
- Password: `admin123`

### 2. Dashboard Mahasiswa
- Menampilkan data diri mahasiswa yang login
- Menampilkan informasi lengkap: NIM, Nama, Email, Telepon, Prodi, dll
- Dapat mengubah email dan password sendiri

## Cara Login Sebagai Mahasiswa

### Langkah 1: Buat User Mahasiswa (dilakukan oleh Admin)

1. Login sebagai admin
2. Buka menu "Mahasiswa" di sidebar
3. Klik "Tambah Mahasiswa"
4. Isi data mahasiswa dan **set password**
5. Simpan

**Contoh:**
- NIM: 666555
- Password: mahasiswa123

### Langkah 2: Login Sebagai Mahasiswa

1. Logout dari admin
2. Login dengan NIM sebagai username
3. Gunakan password yang telah diset oleh admin

**Contoh Login:**
- Username: `666555` (NIM mahasiswa)
- Password: `mahasiswa123` (password yang diset admin)

## Fitur Dashboard Mahasiswa

### Tampilan Profil
Dashboard mahasiswa akan menampilkan:
- Avatar besar (120px)
- Nama lengkap dan NIM
- Program Studi
- Email
- No. Telepon
- Tempat & Tanggal Lahir
- Tahun Masuk
- Alamat Lengkap

### Ubah Email & Password

1. Klik tombol "Ubah Email & Password" di dashboard
2. Atau akses melalui menu "Profil" di sidebar
3. Isi form:
   - **Email**: Email baru (wajib)
   - **Password Baru**: Password baru (opsional, min. 6 karakter)
   - **Konfirmasi Password**: Ulang password (jika mengubah password)

**Validasi:**
- Email harus valid dan belum digunakan user lain
- Password minimal 6 karakter
- Password dan konfirmasi password harus sama
- Password bisa dikosongkan jika hanya ingin ubah email

**Contoh Update:**
```
Email: mahasiswa@example.com
Password Baru: password123456
Konfirmasi Password: password123456
```

## Testing

### Test Dashboard Mahasiswa
1. Login sebagai mahasiswa (NIM: 666555)
2. Dashboard akan menampilkan hanya data mahasiswa tersebut
3. Tidak ada menu statistik atau data mahasiswa lain
4. Hanya bisa melihat dan mengedit data sendiri

### Test Update Profile
1. Login sebagai mahasiswa
2. Klik "Ubah Email & Password" atau menu "Profil"
3. Ubah email dan/atau password
4. Klik "Simpan Perubahan"
5. Akan muncul notifikasi sukses
6. Logout dan login kembali dengan email/password baru

## Catatan Penting

1. **NIM sebagai Username**: Mahasiswa login menggunakan NIM mereka sebagai username
2. **Password Awal**: Password mahasiswa harus diset oleh admin saat pembuatan akun
3. **Update Password**: Mahasiswa bisa mengubah password sendiri kapan saja
4. **Keamanan**: Password di-hash menggunakan Django's password hashing
5. **Role**: Role mahasiswa otomatis ditentukan dari relasi User-Mahasiswa

## API Endpoints

### Get Profile (Mahasiswa)
```
GET /api/auth/profile/
Authorization: Token <token>
```

### Update Profile (Mahasiswa)
```
PUT /api/auth/update-profile/
Authorization: Token <token>
Content-Type: application/json

{
  "email": "newemail@example.com",
  "password": "newpassword123"  // optional
}
```

Response:
```json
{
  "message": "Profile berhasil diupdate",
  "user": {
    "id": 2,
    "username": "666555",
    "email": "newemail@example.com",
    "role": "mahasiswa",
    "nim": {
      "nim": "666555",
      "nama": "Budi Santoso",
      ...
    }
  }
}
```

## Troubleshooting

### Problem: Mahasiswa tidak bisa login
**Solution:** Pastikan admin sudah set password untuk mahasiswa tersebut

### Problem: Dashboard menampilkan error saat login mahasiswa
**Solution:** Pastikan mahasiswa memiliki data lengkap di tabel mahasiswa

### Problem: Update password gagal
**Solution:** 
- Pastikan password minimal 6 karakter
- Pastikan password dan konfirmasi password sama
- Pastikan sudah login dengan token yang valid

### Problem: Mahasiswa melihat data mahasiswa lain
**Solution:** Clear cache browser dan refresh, pastikan menggunakan token yang benar
