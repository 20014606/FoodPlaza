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
        form = FoodForm(request.POST, request.FILES)
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


def deletefood(request, FoodId):
    foods = Food.objects.get(FoodId=FoodId)
    foods.delete()
    return redirect("/allfood")


def getfood(request, FoodId):
    foods = Food.objects.get(FoodId=FoodId)
    return render(request, 'updatefood.html', {'f': foods})


def updatefood(request, FoodId):
    foods = Food.objects.get(FoodId=FoodId)
    form = FoodForm(request.POST, request.FILES, instance=foods)
    if form.is_valid():
        form.save()
        return redirect("/allfood")
    return render(request, 'updatefood.html', {'f': foods})


def login(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        uid = request.POST.get('userId', '')
        upass = request.POST.get('userpass', '')
        utype = request.POST.get('type', '')

        if utype == "Admin":
            for a in Admin.objects.raw('Select * from FP_Admin where AdminId="%s" and AdminPass="%s"' % (uid, upass)):
                if a.AdminId == uid:
                    request.session['AdminId'] = uid
                    return render(request, "index.html", {'success': 'Welcome ' + a.AdminId})
            else:
                return render(request, "login.html", {'failure': 'Incorrect login details'})

        if utype == "User":
            for a in Cust.objects.raw('Select * from FP_Cust where CustEmail="%s" and CustPass="%s"' % (uid, upass)):
                if a.CustEmail == uid:
                    request.session['CustId'] = uid
                    return render(request, "index.html", {'success': 'Welcome ' + a.CustEmail})
            else:
                return render(request, "login.html", {'failure': 'Incorrect login details'})


def doLogout(request):
    key_session = list(request.session.keys())
    for key in key_session:
        del request.session[key]
    return render(request, 'index.html', {'success': 'Logged out successfully'})


def addcust(request):
    if request.method == "POST":
        form = CustForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/login")
            except:
                return render(request, "error.html")
    else:
        form = CustForm()
    return render(request, 'addcust.html', {'form': form})


def showcust(request):
    custs = Cust.objects.all()
    return render(request, 'custlist.html', {'custlist': custs})


def deletecust(request, CustId):
    custs = Cust.objects.get(CustId=CustId)
    custs.delete()
    return redirect("/allcustomer")


def getcust(request):
    print(request.session['CustId'])
    for c in Cust.objects.raw('Select * from FP_Cust where CustEmail="%s"' % request.session['CustId']):
        custs = c
    return render(request, 'updatecust.html', {'c': custs})


def updatecust(request,CustId):
    custs = Cust.objects.get(CustId=CustId)
    form = CustForm(request.POST,instance=custs)
    if form.is_valid():
        form.save()
        session_keys = list(request.session.keys())
        for key in session_keys:
            del request.session[key]
            return redirect("/login")
    return render(request,'updatecust.html',{'c':custs})