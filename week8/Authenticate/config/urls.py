"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from accounts.views import HomeView
from hero.views import IndexPage, HeroListView, HeroDetailView, CreateHero, UpdateHero, DeleteHero

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', HomeView.as_view(), name='home')
    path('', IndexPage.as_view(), name='index'),
    path('hero/', HeroListView.as_view(), name="hero_list"),
    path('hero/<int:pk>', HeroDetailView.as_view()),
    path('hero/add', CreateHero.as_view(), name="add_hero"),
    path('hero/<int:pk>/', UpdateHero.as_view(),  name='update_hero'),
    path('hero/<int:pk>/delete', DeleteHero.as_view(), name="delete_hero")
]
