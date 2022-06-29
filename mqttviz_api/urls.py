from django.urls import path
from .views import CryptoView, CryptoViewUpdate

urlpatterns = [
    path('assets/', CryptoView.as_view()),
    path('assets/<str:item_id>', CryptoView.as_view()),
    path('update/<str:item_id>', CryptoViewUpdate.as_view()),
]