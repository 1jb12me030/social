from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),  # Social login URLs
    path('users/', include('users.urls')),  # User URLs
    path('', include('dashboard.urls')),   # Dashboard URLs
]
