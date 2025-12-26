from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import render

from .models import Prodi, Mahasiswa, User
from .serializers import (
    ProdiSerializer, 
    MahasiswaSerializer, 
    MahasiswaCreateSerializer,
    UserSerializer,
    LoginSerializer,
    RegisterSerializer
)

# Template Views
def home(request):
    """Home page view"""
    return render(request, 'core/home.html')

def about(request):
    """About page view"""
    return render(request, 'core/about.html')


# API Views
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """Login API"""
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        user = authenticate(username=username, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': UserSerializer(user).data
            })
        else:
            return Response({
                'error': 'Username atau password salah'
            }, status=status.HTTP_401_UNAUTHORIZED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """Register API"""
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """Logout API"""
    try:
        request.user.auth_token.delete()
        return Response({'message': 'Logout berhasil'})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    """Get current user profile"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_profile_view(request):
    """Update current user profile (email and password)"""
    user = request.user
    
    # Update email if provided
    if 'email' in request.data:
        email = request.data['email']
        if email:
            # Check if email already exists for another user
            if User.objects.exclude(pk=user.pk).filter(email=email).exists():
                return Response({
                    'error': 'Email sudah digunakan oleh user lain'
                }, status=status.HTTP_400_BAD_REQUEST)
            user.email = email
    
    # Update password if provided
    if 'password' in request.data:
        password = request.data['password']
        if password:
            if len(password) < 6:
                return Response({
                    'error': 'Password minimal 6 karakter'
                }, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(password)
    
    user.save()
    
    return Response({
        'message': 'Profile berhasil diupdate',
        'user': UserSerializer(user).data
    })


class ProdiViewSet(viewsets.ModelViewSet):
    """ViewSet untuk Prodi"""
    queryset = Prodi.objects.all()
    serializer_class = ProdiSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def by_jenjang(self, request):
        """Get prodi by jenjang"""
        jenjang = request.query_params.get('jenjang', None)
        if jenjang:
            prodi = self.queryset.filter(jenjang=jenjang)
            serializer = self.get_serializer(prodi, many=True)
            return Response(serializer.data)
        return Response({'error': 'Parameter jenjang diperlukan'}, status=status.HTTP_400_BAD_REQUEST)


class MahasiswaViewSet(viewsets.ModelViewSet):
    """ViewSet untuk Mahasiswa"""
    queryset = Mahasiswa.objects.select_related('id_prodi').all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MahasiswaCreateSerializer
        return MahasiswaSerializer
    
    @action(detail=False, methods=['get'])
    def by_prodi(self, request):
        """Get mahasiswa by prodi"""
        id_prodi = request.query_params.get('id_prodi', None)
        if id_prodi:
            mahasiswa = self.queryset.filter(id_prodi=id_prodi)
            serializer = MahasiswaSerializer(mahasiswa, many=True)
            return Response(serializer.data)
        return Response({'error': 'Parameter id_prodi diperlukan'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def by_tahun(self, request):
        """Get mahasiswa by tahun masuk"""
        tahun = request.query_params.get('tahun', None)
        if tahun:
            mahasiswa = self.queryset.filter(tahun_masuk=tahun)
            serializer = MahasiswaSerializer(mahasiswa, many=True)
            return Response(serializer.data)
        return Response({'error': 'Parameter tahun diperlukan'}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet untuk User"""
    queryset = User.objects.select_related('nim').all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def by_role(self, request):
        """Get users by role"""
        role = request.query_params.get('role', None)
        if role:
            users = self.queryset.filter(role=role)
            serializer = self.get_serializer(users, many=True)
            return Response(serializer.data)
        return Response({'error': 'Parameter role diperlukan'}, status=status.HTTP_400_BAD_REQUEST)
