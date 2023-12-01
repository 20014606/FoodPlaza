from django.shortcuts import render, redirect
from django.db import connection, transaction
from Foodapp.forms import FoodForm,CustForm,AdminForm,CartForm,OrderForm
from Foodapp.models import Food,Cust,Admin,Cart,Order
import datetime

cursor = connection.cursor()

# Create your views here.


def foodapp(request):
    return render(request,'index.html')


def addfood(request):
    if request.method == "POST":
        form = FoodForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect("/allfood")
            except:
                return render(request,"error.html")
        else:
            form = FoodForm()
    return render(request,'addfood.html',{'form': form})


def showfood(request):
    foods = Food.objects.all()
    return render(request, 'foodlist.html', {'foodlist': foods})

