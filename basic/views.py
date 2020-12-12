from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Enquiry , Product , Employee , Client , Slip , Service , Category
from .forms import ProductForm , EnquiryForm , EmployeForm , SignUpForm  , NewClient , NewSlip , NewService
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime


def home(request):
    return render(request  , 'basic/homepage.html')