from tkinter import Y
from django.db import models
from matplotlib.contour import ContourSet
from matplotlib.style import available

# Create your models here.

class Buy(models.Model):
    firstname1 = models.CharField(max_length=100)
    lastname1 = models.CharField(max_length=100)
    course1 = models.CharField(max_length=100)
    idnum1 = models.CharField(max_length=100)
    contact1 = models.CharField(max_length=100)
    email1 = models.CharField(max_length=100)
    order1 = models.CharField(max_length=100)
    quantity1 = models.CharField(max_length=100)
    size1 = models.CharField(max_length=100)


class Reserve(models.Model):
    firstname2 = models.CharField(max_length=100)
    lastname2 = models.CharField(max_length=100)
    course2 = models.CharField(max_length=100)
    idnum2 = models.CharField(max_length=100)
    contact2 = models.CharField(max_length=100)
    email2 = models.CharField(max_length=100)
    reserve2 = models.CharField(max_length=100) 
    dateofreserve2 = models.CharField(max_length=100)
    dateofendreserve2 = models.CharField(max_length=100)
    timeofreserve2 = models.CharField(max_length=100)
    timeofendreserve2 = models.CharField(max_length=100)

class Borrow(models.Model):
    firstname3 = models.CharField(max_length=100)
    lastname3 = models.CharField(max_length=100)
    course3 = models.CharField(max_length=100)
    idnum3 = models.CharField(max_length=100)
    contact3 = models.CharField(max_length=100)
    email3 = models.CharField(max_length=100)
    equipment3 = models.CharField(max_length=100) 
    dateofborrow3 = models.CharField(max_length=100)
    dateofreturn3 = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Equipments(models.Model):
    equipments = models.CharField(max_length=100)
    quantity = models.IntegerField()
    borrowed = models.IntegerField()
    available = models.IntegerField()

class Sales(models.Model):
    order1 = models.CharField(max_length=100)
    quantity = models.IntegerField()
    sales = models.IntegerField()


class Registration(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    idnum = models.CharField(max_length=100)

class Prices(models.Model):
    item  = models.CharField(max_length=100)
    price = models.IntegerField()