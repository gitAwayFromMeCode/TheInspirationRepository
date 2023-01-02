from django.urls import path
from .views import QuoteListView, QuoteDetailView, QuoteCreateView, QuoteUpdateView, QuoteDeleteView, UserQuoteListView
from . import views

urlpatterns = [
    path('', QuoteListView.as_view(), name='quote-home'),
    path('user/<str:username>', UserQuoteListView.as_view(), name='user-quotes'),
    path('quote/<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),
    path('quote/new/', QuoteCreateView.as_view(), name='quote-create'),
    path('quote/<int:pk>/update/', QuoteUpdateView.as_view(), name='quote-update'),
    path('quote/<int:pk>/delete/', QuoteDeleteView.as_view(), name='quote-delete'),
    path('about/', views.about, name='quote-about'),
]