from django.shortcuts import render
from .models import *
from .forms import *
from django.http import JsonResponse
# Create your views here.

def homeView(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'financeApp/homeView.html', context)


def userView(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'financeApp/userView.html', context)
    
def moneyView(request, pk):
    money = Money.objects.get(id=pk)
    context = {'money':money}
    return render(request, 'financeApp/moneyView.html', context)

def addMoney(request, pk):
    money = Money.objects.get(id=pk)
    context = {'money':money}
    return render(request, 'financeApp/addTransaction.html', context)
