from pyexpat import model
from statistics import mode
from django import forms
from .models import *
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = '__all__'

class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = '__all__'

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = '__all__'
        
class EquipForm(forms.ModelForm):
    class Meta:
        model = Equipments
        fields = '__all__'

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        

class PriceForm(forms.ModelForm):
    class Meta:
        model = Prices
        fields = '__all__'
        
# class CreateUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['first_name','last_name','username', 'password1', 'password2']