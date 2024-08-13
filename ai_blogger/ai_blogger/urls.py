from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('blog.urls')),
    path('login/', include('blog.urls')),
    path('dashboard/', include('blog.urls')),
]
