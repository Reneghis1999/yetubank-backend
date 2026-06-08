from django.urls import path
from .views import (
    TransferView,
    TransactionListView
)

urlpatterns = [
    path('transfer/', TransferView.as_view()),

    path('transactions/', TransactionListView.as_view()),
]