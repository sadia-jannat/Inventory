"""
URL configuration for inventory_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path,include
from inentory_app import views

#image ar jonno
from django.conf import settings
from django.conf.urls.static import static

#API
from inentory_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.stuff_signup, name='stuff_signup'),
    path('stuff_login/', views.stuff_login, name='stuff_login'),
    path('stuff_logout/', views.stuff_logout, name='stuff_logout'),
    path('home/', views.Home, name='Homepage'),
    path('deviceaddpage/', views.DeviceAddForm, name='DeviceAddForm'),
    path('userpage/', views.Dashboard, name='Dashboard'),
    path('dashboard_delete/<int:id>/', views.dashboard_delete, name='dashboard_delete'),
    path('dashboard_edit/<int:id>/', views.dashboard_edit, name='dashboard_edit'),
    path('search/', views.search, name="search"),
    path('sale_add/', views.sale_add, name='sale_add'),
    path('sale_details/', views.sale_details, name='sale_details'),
   
    
]

#image ar jonno
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
