from pkgutil import get_data
from webbrowser import get
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
from .forms import *

from django.core.mail import send_mail

# LOGIN AND REGISTER
def loginuser(request):
    userdb = Registration.objects.values_list('username', flat=True)
    passwrd_db = Registration.objects.values_list('password1', flat=True)

    usernames = request.POST.get('user')
    passto = request.POST.get('pass')

    for i in range(len(userdb)):
        if userdb[i] == usernames and passwrd_db[i] == passto:
            request.session['username'] = usernames
            return redirect('student')

        elif usernames == "admin" and passto == "admin":
            return redirect ('admin_home')

    context = {}

    return render(request, "login.html", context)

def register(request):
    regform = RegistrationForm(request.POST or None)

    pass1 = request.POST.get('password1')
    pass2 = request.POST.get('password2')

    if pass1 != pass2:
        return redirect('registration')

    if regform.is_valid():
        regform.save()
        return redirect('login')


    context = {
        
    }

    return render(request, "registration.html", context)


# STUDENT

def student(request):
    formbuy = BuyForm(request.POST or None)
    formreserve = ReserveForm(request.POST or None)
    formborrow = BorrowForm(request.POST or None)
    getUser = request.session['username']
    checkData = Registration.objects.filter(username=getUser)

    getPrice1 = Prices.objects.filter(item = 'P.E Shirt and Jogging Pants').values()
    getPrice2 = Prices.objects.filter(item = 'P.E Shirt and Shorts').values()
    
    listData = []
    for i in checkData:
        listData.append(i)
    

    getFName = request.POST.get('firstname1')
    getOrder = request.POST.get('order1')
    check1 = Buy.objects.filter(firstname1 = getFName).values()

    
    list1 = []
    list2 = []

    for p1 in getPrice1:
        list1.append(p1['price'])
    for p2 in getPrice2:
        list2.append(p2['price'])
    
    val1 = list1[0]
    val2 = list2[0]

    for a in check1:
        getQuantity1 = a['quantity1']
        print(getQuantity1)
        if getOrder == "P.E Shirt and Jogging Pants":
            getTots1 = int(getQuantity1) * int(val1)
            Sales.objects.filter(order1 = getOrder).update(quantity =+ int(getQuantity1), sales=+int(getTots1))
        else:
            getTots2 = int(getQuantity1) * int(val2)
            Sales.objects.filter(order1 = getOrder).update(quantity =+ int(getQuantity1), sales=+int(getTots2))

    getEquipment = request.POST.get('equipment3')
    check3 = Equipments.objects.filter(equipments = getEquipment).values()

    for x in check3: 
        getQuants = x['quantity']
        getBorrowed = x['borrowed']
        getAvail = x['available']

        totalQuants = getQuants - 1
        totalBorrowed = getBorrowed + 1
        totalAvail = getAvail - 1

        Equipments.objects.filter(equipments = getEquipment).update(quantity = totalQuants, borrowed = totalBorrowed, available = totalAvail)

    getDataInventory = Equipments.objects.all()
    getdata ={
        'inventory': getDataInventory,
        'student': listData
    }

    if formbuy.is_valid():
        formbuy.save()
        return redirect('student')

    if formreserve.is_valid():
        formreserve.save()
        return redirect('student')

    if formborrow.is_valid():
        formborrow.save()
        return redirect('student')
    
    return render(request, "student.html", getdata)

# ADMIN

def adminHome(request):
    return render(request, "admin_homepage.html")

def adminBorrow(request):
    borrow_db = Borrow.objects.all()
    getdata ={
        'borrow_data': borrow_db
    }
    ids = request.POST.get('getId')
    stat = request.POST.get('equips')
    Borrow.objects.filter(id = ids).update(status=stat)

    return render(request, "admin_borrow.html", getdata)

def adminReturn(request):
    check = Borrow.objects.filter(status = 'Returned').values()

    returnData = []
    for x in check:
        returnData.append(x)

    context = {
        'return': returnData
    }
   
    return render(request, "admin_return.html", context)

def adminSched(request):
    reserve_db = Reserve.objects.all()
    getdata ={
        'reserve_data': reserve_db
    }
    return render(request, "admin_schedule.html", getdata)

def adminPreorder(request):
    buy_db = Buy.objects.all()
    getdata ={
        'buy_data': buy_db
    }
    return render(request, "admin_preorder.html", getdata)

def adminBlock(request):
    check = Borrow.objects.filter(status = 'Black Listed').values()

    returnData = []
    for x in check:
        returnData.append(x)

    context = {
        'black': returnData
    }
    return render(request, "admin_blocklisted.html" , context)

def adminInventory(request):
    getPrice1 = Prices.objects.filter(item = 'P.E Shirt and Jogging Pants').values()
    getPrice2 = Prices.objects.filter(item = 'P.E Shirt and Shorts').values()
    
    getD1 = request.POST.get('pe1')
    getD2 = request.POST.get('pe2')

    getP1 = request.POST.get('joggingpants')     
    getP2 = request.POST.get('shorts')  

    Prices.objects.filter(item = getD1).update(price = getP1)
    Prices.objects.filter(item = getD2).update(price = getP2)

    getDataInventory = Equipments.objects.all()
    getdata ={
        'inventory': getDataInventory,
        'price1': getPrice1,
        'price2': getPrice2
    }

    equips = EquipForm(request.POST or None)
    if equips.is_valid():
        equips.save()

    return render(request, "admin_inventory.html", getdata)

def adminSales(request):
    getTotal = Sales.objects.all()

    context = {
        'totalsales': getTotal
    }
    return render(request, "admin_totalsales.html", context)



def sendmail_sheesh( request):
    if request.method == 'POST':
        emailss = request.POST.getlist('checked')
        send_mail('NSTP Documents', 
                'Hello this is an email from P.E Department. We are here to notify you about Your Reservation of Court! Please present this email upon entering on court. Thank you',
                'NSTP',
                 ((emailss)),
                fail_silently=False)
        
        print(emailss)
    return redirect('/admin_schedule')