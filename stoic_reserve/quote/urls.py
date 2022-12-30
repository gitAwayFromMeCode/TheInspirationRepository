from django.urls import path
from .views import QuoteListView, QuoteDetailView, QuoteCreateView, QuoteUpdateView
from . import views

urlpatterns = [
    path('', QuoteListView.as_view(), name='quote-home'),
    path('quote/<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),
    path('quote/new/', QuoteCreateView.as_view(), name='quote-create'),
    path('quote/<int:pk>/update/', QuoteUpdateView.as_view(), name='quote-update'),
    path('about/', views.about, name='quote-about'),
]