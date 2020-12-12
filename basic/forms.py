from django.forms import ModelForm
from basic.models import Product , Enquiry , Employee , Client  , Slip ,Service
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewService(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        
class NewSlip(ModelForm):
    class Meta:
        model = Slip
        fields = '__all__'
        

class NewClient(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class SignUpForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class EnquiryForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'


class EmployeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

      