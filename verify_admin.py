import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import User

# Cek user admin
admin = User.objects.get(username='admin')

print("\n" + "="*60)
print("DATA USER ADMIN")
print("="*60)
print(f"Username    : {admin.username}")
print(f"Name        : {admin.name}")
print(f"Role        : {admin.role}")
print(f"Is Active   : {admin.is_active}")
print(f"Is Staff    : {admin.is_staff}")
print(f"Is Superuser: {admin.is_superuser}")
print(f"Has Password: {bool(admin.password)}")
print("="*60)

# Test password
if admin.check_password('admin123'):
    print("\n✅ Password 'admin123' BENAR!")
else:
    print("\n❌ Password 'admin123' SALAH!")
    print("   Melakukan reset ulang...")
    admin.set_password('admin123')
    admin.save()
    print("   ✅ Password berhasil direset!")

print("\n📝 Gunakan kredensial ini untuk login:")
print("   Username: admin")
print("   Password: admin123")
print("   URL: http://localhost:5173")
