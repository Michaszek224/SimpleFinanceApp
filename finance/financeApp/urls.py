from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='homeView'),
    path('user/addUser', addUser, name='addUser'),
    path('user/<str:pk>/', userView, name='userView'),
    path('user/<str:pk>/add/', addMoney, name='addMoney'),
    path('user/<str:pk>/add/addTransaction', addMoneyPost, name='addTransaction'),
    path('money/<str:pk>/', moneyView, name='moneyView'),
    path('money/<str:pk>/delete/', deleteMoney, name= 'deleteMoney'),
    path('money/<str:pk>/newMoney/', newMoney, name='newMoney'),
    path('money/<str:pk>/newMoney/newMoneyAdd/', newMoneyAdd, name='newMoneyAdd'),
    path('user/<str:pk>/delete/', deleteUser, name='deleteUser'),
]