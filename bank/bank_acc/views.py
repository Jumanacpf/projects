from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import account


# Create your views here.
def acc(request):
    if request.method=='POST':
        accno=int(request.POST['account'])
        name =request.POST['name']
        email =request.POST['email']
        amount= int(request.POST['amount'])
        if amount>1000:
            bank=account.objects.create(accno=accno,name=name,email=email,amount=amount)
            bank.save()
            return render(request, 'account.html')
            # return HttpResponse("Account Created")
        else:
            return HttpResponse("Minimum balance must be 1000")

    else:
        return render(request,'account.html')

def add(request):
    if request.method == 'POST':
        accno=int(request.POST['account'])
        addam=int(request.POST['addam'])
        bank=account.objects.get(accno=accno)
        if addam>100:
            newamount=addam+bank.amount
            bank.amount=newamount
            bank.save()
            return render(request,'add.html')
            # return HttpResponse("Amount added successfully")
        else:
            return HttpResponse("Minimum balance must be 1000")
    else:
        return render(request,'add.html')

def withdraw(request):
    if request.method == 'POST':
        accno=int(request.POST['account'])
        wdraw=int(request.POST['wdraw'])
        bank=account.objects.get(accno=accno)
        if wdraw%100==0 or wdraw%200==0 or wdraw%400==0:
            newamount=bank.amount-wdraw
            bank.amount=newamount
            bank.save()
            return render(request, 'withdraw.html',{})
            # return HttpResponse("Withdraw money successfully")
        else:
            return HttpResponse("Minimum balance is 1000")
    else:
        return render(request,'withdraw.html')

def balance(request):


    if request.method == 'POST':
        accno=request.POST['accno']
        data = account.objects.get(accno=accno)
        return render(request, 'balance.html', {'data': data.amount})
    else:
        return render(request,'balance.html')


def home(request):
    return render(request,'home.html')

