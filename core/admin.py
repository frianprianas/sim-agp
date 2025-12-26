from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Prodi, Mahasiswa, User

# Register your models here.

@admin.register(Prodi)
class ProdiAdmin(admin.ModelAdmin):
    list_display = ('id_prodi', 'prodi', 'jenjang', 'created_at')
    list_filter = ('jenjang',)
    search_fields = ('prodi',)
    ordering = ('jenjang', 'prodi')


@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('nim', 'nama', 'id_prodi', 'jenis_kelamin', 'tahun_masuk', 'email')
    list_filter = ('jenis_kelamin', 'tahun_masuk', 'id_prodi')
    search_fields = ('nim', 'nama', 'email')
    ordering = ('-tahun_masuk', 'nama')
    
    fieldsets = (
        ('Identitas', {
            'fields': ('nim', 'nama', 'jenis_kelamin')
        }),
        ('Data Kelahiran', {
            'fields': ('tempat', 'tgl_lahir')
        }),
        ('Akademik', {
            'fields': ('id_prodi', 'tahun_masuk')
        }),
        ('Kontak', {
            'fields': ('alamat', 'email', 'no_telepon')
        }),
    )


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'name', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'name', 'email')
    ordering = ('username',)
    
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal Info', {
            'fields': ('name', 'email', 'role', 'nim')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login',)
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'email', 'role', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    
    filter_horizontal = ('groups', 'user_permissions')
