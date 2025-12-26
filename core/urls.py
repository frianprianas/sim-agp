from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'core'

# Router untuk API
router = DefaultRouter()
router.register(r'prodi', views.ProdiViewSet, basename='prodi')
router.register(r'mahasiswa', views.MahasiswaViewSet, basename='mahasiswa')
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns = [
    # Template URLs
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # API URLs
    path('api/', include(router.urls)),
    path('api/auth/login/', views.login_view, name='api_login'),
    path('api/auth/register/', views.register_view, name='api_register'),
    path('api/auth/logout/', views.logout_view, name='api_logout'),
    path('api/auth/profile/', views.profile_view, name='api_profile'),
    path('api/auth/update-profile/', views.update_profile_view, name='api_update_profile'),
]
