from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  # Custom login view
    path('logout/', views.user_logout, name='logout'),  # Logout view
    path('profile/', views.profile, name='profile'),
]
