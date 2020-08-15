from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('stats/', include('stats.urls')),
    path('users/', include('users.urls')),
]
