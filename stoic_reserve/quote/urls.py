from django.urls import path
from .views import QuoteListView, QuoteDetailView, QuoteCreateView
from . import views

urlpatterns = [
    path('', QuoteListView.as_view(), name='quote-home'),
    path('quote/<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),
    path('quote/new/', QuoteCreateView.as_view(), name='quote-create'),
    path('about/', views.about, name='quote-about'),
]