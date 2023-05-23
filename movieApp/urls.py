"""
URL configuration for djangoProjectORM8 project.

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
from django import views
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from .import views

app_name = 'movieApp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fp/', views.first_page),
    path('', views.show_all_movies, name='movie-detail_all'),
    path('movies/<int:id_movie>', views.show_one_movie, name='movie-detail'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('feedback/', views.feedback, name='feedback'),
    path('done/', views.done, name='done'),
    path('table/', views.table, name='table'),
]