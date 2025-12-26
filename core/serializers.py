from rest_framework import serializers
from .models import Prodi, Mahasiswa, User


class ProdiSerializer(serializers.ModelSerializer):
    """Serializer untuk Prodi"""
    class Meta:
        model = Prodi
        fields = '__all__'


class MahasiswaSerializer(serializers.ModelSerializer):
    """Serializer untuk Mahasiswa"""
    prodi_detail = ProdiSerializer(source='id_prodi', read_only=True)
    
    class Meta:
        model = Mahasiswa
        fields = '__all__'


class MahasiswaCreateSerializer(serializers.ModelSerializer):
    """Serializer untuk create/update Mahasiswa"""
    password = serializers.CharField(write_only=True, required=False, allow_blank=True, min_length=6)
    
    class Meta:
        model = Mahasiswa
        fields = '__all__'
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        mahasiswa = super().create(validated_data)
        
        # Create user account for mahasiswa if password provided
        if password:
            User.objects.create_user(
                username=mahasiswa.nim,
                name=mahasiswa.nama,
                password=password,
                role='mahasiswa',
                nim=mahasiswa
            )
        
        return mahasiswa
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        mahasiswa = super().update(instance, validated_data)
        
        # Update user account if exists and password provided
        if password:
            try:
                user = User.objects.get(nim=mahasiswa)
                user.set_password(password)
                user.name = mahasiswa.nama  # Update name too
                user.save()
            except User.DoesNotExist:
                # Create user if doesn't exist
                User.objects.create_user(
                    username=mahasiswa.nim,
                    name=mahasiswa.nama,
                    password=password,
                    role='mahasiswa',
                    nim=mahasiswa
                )
        
        return mahasiswa


class UserSerializer(serializers.ModelSerializer):
    """Serializer untuk User"""
    mahasiswa_detail = MahasiswaSerializer(source='nim', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'role', 'nim', 'mahasiswa_detail', 'created_at']
        read_only_fields = ['id', 'created_at']


class LoginSerializer(serializers.Serializer):
    """Serializer untuk Login"""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer untuk Register"""
    password = serializers.CharField(write_only=True, min_length=6)
    password_confirmation = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password', 'password_confirmation', 'role', 'nim']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({"password": "Password tidak cocok"})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
