from django.shortcuts import render, redirect
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

def addTransaction(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        transactionAmount = float(request.POST.get('transaction', 0.0))
        money = Money.objects.create(user=user, balance=transactionAmount, lastTransaction=transactionAmount)
        money.save()

        return redirect('userView', pk=user.id)
    context = {'user':user}
    return render(request, 'finance/addTransaction.html', context)