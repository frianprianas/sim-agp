import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Mahasiswa, Prodi

# Get first prodi
prodi = Prodi.objects.first()
print(f"\n✅ Prodi found: {prodi}")

# Test create mahasiswa with minimal data
test_data = {
    'nim': '12345678',
    'nama': 'Test Mahasiswa',
    'id_prodi': prodi,
    'tahun_masuk': 2024
}

try:
    # Check if already exists
    if Mahasiswa.objects.filter(nim=test_data['nim']).exists():
        print(f"\n⚠️  Mahasiswa dengan NIM {test_data['nim']} sudah ada, menghapus...")
        Mahasiswa.objects.filter(nim=test_data['nim']).delete()
    
    mahasiswa = Mahasiswa.objects.create(**test_data)
    print(f"\n✅ Mahasiswa berhasil dibuat: {mahasiswa}")
    print(f"   NIM: {mahasiswa.nim}")
    print(f"   Nama: {mahasiswa.nama}")
    print(f"   Prodi: {mahasiswa.id_prodi.prodi}")
    print(f"   Tahun Masuk: {mahasiswa.tahun_masuk}")
    
    # Clean up
    mahasiswa.delete()
    print(f"\n✅ Test mahasiswa berhasil dihapus")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
