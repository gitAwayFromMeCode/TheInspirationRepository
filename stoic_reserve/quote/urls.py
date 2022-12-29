from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quote-home'),
    path('about/', views.about, name='quote-about'),
]