"""Treesform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from fillform import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 



urlpatterns = [
    path('', views.home, name='home'),
    path('fillform/', include('fillform.urls'), name='index'),
    path('.well-known/acme-challenge/gsqL-gO2lzDEqGFlXNSWr2kWBTKEKd5jaKpJmJO1IW0', views.ssl, name='ssl'),
    path('.well-known/acme-challenge/poLvXQi6T6fSFyu8A3J6Q9h4Q5eOHCXe1GntnwCbBno', views.ssl2, name='ssl2'),
    # path('admin/', admin.site.urls),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
