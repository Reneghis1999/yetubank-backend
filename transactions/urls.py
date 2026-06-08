from django.urls import path
from .views import (
    TransferView,
    TransactionListView,
    DashboardStatsView
)
urlpatterns = [
    path('transfer/', TransferView.as_view()),

    path('transactions/', TransactionListView.as_view()),

    path('dashboard/stats/', DashboardStatsView.as_view()),
]