from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='homeView'),
    path('user/<str:pk>/', userView, name='userView'),
    path('money/<str:pk>/', moneyView, name='moneyView'),
    path('money/<str:pk>/add/', addMoney, name='addMoney')
]