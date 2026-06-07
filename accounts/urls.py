from django.urls import path
from .views import AccountDetailView

urlpatterns = [
    path('me/', AccountDetailView.as_view()),
]