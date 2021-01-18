from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.mcs, name='users'),
    path('seed/', views.seed)
]
