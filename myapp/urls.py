"""

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
from django.conf.urls import include
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path,re_path
from app import views
from django.conf.urls import include
urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls'))
]
=======
from django.urls import path
from app import views


app_name = "app"
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('importFile/', views.importFile, name='importFile'),
    path('uploadFile/', views.uploadFile, name='uploadFile'),
    path('downloadFile/', views.downloadFile, name='downloadFile'),
   
]
>>>>>>> 17c62db8abd3ed36306db273f06dd70b152bbd4b
