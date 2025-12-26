import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import User

print("\n" + "="*60)
print("DAFTAR USER ADMIN")
print("="*60)

admins = User.objects.filter(is_superuser=True)

if admins.exists():
    for i, admin in enumerate(admins, 1):
        print(f"\n{i}. Username: {admin.username}")
        print(f"   Nama    : {admin.name}")
        print(f"   Role    : {admin.role}")
        print(f"   Staff   : {'Ya' if admin.is_staff else 'Tidak'}")
        print(f"   Aktif   : {'Ya' if admin.is_active else 'Tidak'}")
else:
    print("\nTidak ada admin ditemukan!")

print("\n" + "="*60)
print(f"Total Admin: {admins.count()}")
print("="*60)

print("\n⚠️  Untuk login, gunakan:")
print("   Username: admin")
print("   Password: admin123")
print("   (Dibuat via createsuperuser)")
