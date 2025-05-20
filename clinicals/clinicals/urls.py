"""
URL configuration for clinicals project.

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
from clinicalsApp.views import PatientListView, PatientCreateView, PatientUpdateView, PatientDeleteView
from clinicalsApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PatientListView.as_view(), name='index'),
    path('create/', PatientCreateView.as_view(), name='PatientCreateView'),
    path('update/<int:pk>/', PatientUpdateView.as_view(), name='PatientUpdateView'),
    path('delete/<int:pk>/', PatientDeleteView.as_view(), name='PatientDeleteView'),
    path('addData/<int:pk>/', views.addData, name='addData'),
    path('analyze/<int:pk>/', views.analyze, name='analyze'),
]
