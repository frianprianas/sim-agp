import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Prodi, Mahasiswa, User

print('=' * 50)
print('DATABASE CONNECTION TEST')
print('=' * 50)

# Test Prodi
print('\n📚 PROGRAM STUDI:')
print('-' * 50)
prodi_list = Prodi.objects.all()
print(f'Total: {prodi_list.count()}')
for p in prodi_list:
    print(f'  {p.id_prodi}. {p.prodi} ({p.jenjang})')

# Test Mahasiswa
print('\n👥 MAHASISWA:')
print('-' * 50)
mhs_list = Mahasiswa.objects.all()
print(f'Total: {mhs_list.count()}')
for m in mhs_list:
    print(f'  {m.nim} - {m.nama} ({m.id_prodi.prodi})')

# Test Users
print('\n👨‍💼 USERS:')
print('-' * 50)
user_list = User.objects.all()
print(f'Total: {user_list.count()}')
for u in user_list:
    print(f'  {u.username} - {u.name} [{u.role}]')

print('\n' + '=' * 50)
print('✅ DATABASE CONNECTION SUCCESS!')
print('=' * 50)
