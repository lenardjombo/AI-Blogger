from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.redirect_to_login, name='home'),  # Redirect to login page
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('generate_content/', views.generate_content, name='generate_content'),  # Add this line
]

