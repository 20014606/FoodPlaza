from django.shortcuts import render, redirect
from django.db import connection, transaction
from Foodapp.forms import FoodForm,CustForm,AdminForm,CartForm,OrderForm
from Foodapp.models import Food,Cust,Admin,Cart,Order
import datetime

cursor = connection.cursor()

# Create your views here.


def foodapp(request):
    return render(request,'index.html')
