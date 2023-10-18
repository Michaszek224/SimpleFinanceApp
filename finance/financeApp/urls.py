from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='homeView'),
    path('user/<str:pk>/', userView, name='userView'),
    path('user/<str:pk>/add/', addMoney, name='addMoney'),
    path('user/<str:pk>/add/addTransaction', addTransaction, name='addTransaction'),
    path('money/<str:pk>/', moneyView, name='moneyView'),
]