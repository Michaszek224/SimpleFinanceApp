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
    user = User.objects.get(id = pk)

    try:
        money = Money.objects.get(user=user)
    except Money.DoesNotExist:
        money = Money.objects.create(user=user, balance=0, lastTransaction=0)
    context = {'money':money}
    return render(request, 'financeApp/addTransaction.html', context)

def addMoneyPost(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        transactionAmount = float(request.POST.get('transaction', 0.0))
        money = Money.objects.create(user=user, balance=transactionAmount, lastTransaction=transactionAmount)
        money.save()

        return redirect('userView', pk=user.id)
    context = {'user':user}
    return render(request, 'finance/addTransaction.html', context)

def deleteMoney(request, pk):
    money = Money.objects.get(id = pk)

    if request.method == 'POST':
        money.delete()
        return redirect('userView', pk = money.user.id)
    context = {'money': money}
    return render(request, 'financeApp/deleteMoney.html', context)

def newMoney(request, pk):
    money = Money.objects.get(id = pk)
    context={'money':money}
    return render(request, 'financeApp/newMoney.html', context)

def newMoneyAdd(request, pk):
    money = Money.objects.get(id = pk)
    if request.method == 'POST':
        moneyAmount = float(request.POST.get('moneyInput', 0.0))
        currentBalance = money.balance
        money.lastTransaction = moneyAmount
        money.balance = float(currentBalance) + moneyAmount
        money.save()
        return redirect('moneyView', pk=money.id)

    context = {'money':money}
    return render(request, 'financeApp/newMoney.html', context)

def addUser(request):
    if request.method == 'POST':
        name = request.POST.get('nameInput')
        surname = request.POST.get('surnameInput')

        userCurrent = User(name = name, surname = surname)
        userCurrent.save()
        money = Money(user = userCurrent, balance = 0, lastTransaction = 0)
        money.save()
        return redirect('homeView')
    
    return render(request, 'financeApp/newUser.html')