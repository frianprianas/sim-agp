from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class Prodi(models.Model):
    """Model untuk Program Studi"""
    JENJANG_CHOICES = [
        ('D3', 'Diploma 3'),
        ('S1', 'Sarjana'),
    ]
    
    id_prodi = models.BigAutoField(primary_key=True)
    prodi = models.CharField(max_length=100)
    jenjang = models.CharField(max_length=2, choices=JENJANG_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        db_table = 'prodi'
        verbose_name = 'Program Studi'
        verbose_name_plural = 'Program Studi'
    
    def __str__(self):
        return f"{self.prodi} ({self.jenjang})"


class Mahasiswa(models.Model):
    """Model untuk Mahasiswa"""
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]
    
    nim = models.CharField(max_length=20, primary_key=True)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN_CHOICES)
    tempat = models.CharField(max_length=50, verbose_name='Tempat Lahir')
    tgl_lahir = models.DateField(verbose_name='Tanggal Lahir')
    id_prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE, db_column='id_prodi')
    tahun_masuk = models.IntegerField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    no_telepon = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        db_table = 'mahasiswa'
        verbose_name = 'Mahasiswa'
        verbose_name_plural = 'Mahasiswa'
        ordering = ['-tahun_masuk', 'nama']
    
    def __str__(self):
        return f"{self.nim} - {self.nama}"


class CustomUserManager(BaseUserManager):
    """Custom user manager"""
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Username harus diisi')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser harus memiliki is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser harus memiliki is_superuser=True.')
        
        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model"""
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('mahasiswa', 'Mahasiswa'),
    ]
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='mahasiswa')
    nim = models.OneToOneField(
        Mahasiswa, 
        on_delete=models.CASCADE, 
        db_column='nim',
        to_field='nim',
        null=True, 
        blank=True,
        related_name='user'
    )
    remember_token = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    # Required for Django Admin
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f"{self.username} - {self.name}"
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.username
