from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout')
]