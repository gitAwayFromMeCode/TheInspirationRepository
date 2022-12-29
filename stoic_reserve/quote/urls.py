from django.urls import path
from .views import QuoteListView, QuoteDetailView
from . import views

urlpatterns = [
    path('', QuoteListView.as_view(), name='quote-home'),
    path('quote/<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),
    path('about/', views.about, name='quote-about'),
]