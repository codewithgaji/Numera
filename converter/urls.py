from django.urls import path
from . import views

urlpatterns = [
    path('convert/', views.converter, name='convert'),
    path('', views.home, name='home'),
]
