"""placesRemember URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from tkinter.font import names
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

""" Add views and URLs """
from user.views import *
from post.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('user.urls', namespace='accounts')),
    path('', include('post.urls', namespace='posts')),
    path('auth/', include('social_django.urls', namespace='social')), #<--
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
