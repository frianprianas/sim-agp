import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import User

# Reset password untuk admin
try:
    admin = User.objects.get(username='admin')
    admin.set_password('admin123')
    admin.save()
    print("\n✅ Password admin berhasil direset!")
    print("   Username: admin")
    print("   Password: admin123")
except User.DoesNotExist:
    print("\n❌ User admin tidak ditemukan!")
    print("   Membuat user admin baru...")
    
    admin = User.objects.create_user(
        username='admin',
        password='admin123',
        name='Administrator',
        role='admin'
    )
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()
    
    print("\n✅ User admin berhasil dibuat!")
    print("   Username: admin")
    print("   Password: admin123")
