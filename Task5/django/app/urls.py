"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('profile/<int:profile_id>', views.profile, name='profile'),
    path('profiles/', views.all_profiles, name='profiles'),
    path('inventory/<int:character_id>', views.inventory, name='inventory'),
    path('inventories/', views.all_inventories, name='inventories'),
    path('character/', views.character, name='character'),
    path('characters/', views.all_characters, name='characters'),
    path('create_item/', views.create_item, name='create_item'),
    path('error/', views.error, name='error')
]
