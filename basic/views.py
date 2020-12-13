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


def reports(request):
    warm = Enquiry.objects.filter(response ='warm').count()
    cold = Enquiry.objects.filter(response ='cold').count()
    normal = Enquiry.objects.filter(response ='normal').count()
    print(warm)
    params = {
        'warm': warm,
        'cold' : cold , 
        'normal': normal
    }
    return render(request , 'basic/reports.html' , params)
def service(request):
    service = Service.objects.all()
    form = NewService()
    if request.method == 'POST':
        form = NewService(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return render(request , 'basic/404.html')
    else:
        form = NewService()
    params = {
        'service': service,
        'form' : form,
        'today' : today
    }
    return render(request , 'basic/forms/service.html', params)
def followup(request):
    obj = Product.objects.all()
    cli = Client.objects.all()
    
    l1 = []
    for i in obj:
        if i.quantity <5:
            l1.append(i)
    
   
    params = {
        'pro' : l1,
        'cli': cli    }
    return render(request , 'basic/followup/followupBase.html' , params)



def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        user = authenticate(username=uname , password = pwd)

        if user is not None:
            login(request , user)
            return redirect('cover')
        else:
            return render(request , 'basic/404.html')
    else :
        pass

    return render(request , 'basic/signin.html')

def register(request):
    form = SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('calendarapp:index')
        else:
            return HttpResponse("Nai hua bhau")
    else :
        form = SignUpForm()
    params = {
    'form': form
    }

    return render(request , 'basic/register.html' , params )
    
     
def profilePage(request):
    return render(request , 'basic/profile.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')
@login_required(login_url='loginPage')
def cover(request):
    return render(request , 'basic/cover.html')
def home(request):
    today = datetime.now()
    enq = Enquiry.objects.all()
    service  = Service.objects.all()
    pro = Product.objects.all().order_by('quantity')
    empCount = Employee.objects.count()
    clients = Client.objects.count()
    services = Service.objects.count()
    params = {
        'enq': enq ,
        'pro' : pro,
        'empCount' : empCount,
        'Clients' : clients,
        'services': services,
        'service': service, 
        'today' : today
    }
    return render(request , 'basic/homepage.html' , params)


@login_required(login_url='loginPage')
def enquiry(request):
    enq = Enquiry.objects.all()
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')
        else :
            return HttpResponse('<h3> Try again </h3>')
    else :
        form = EnquiryForm()
    params = {
        'form' : form ,
        'pro' : enq
    }

    return render(request , 'basic/enquiry.html' , params)
@login_required(login_url='loginPage')
def enquiryUpdate(request , pk):
    enq = Enquiry.objects.get(id = pk)
    
    if request.method == 'POST':
        form = EnquiryForm(request.POST , instance=enq)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = EnquiryForm(instance= enq)
    params = {
        'form' : form
    }
    return render(request , 'basic/enquiryForm.html' , params)

@login_required(login_url='loginPage')
def deleteEnquiry(request , pk):
    pro = Enquiry.objects.get(id=pk)
    if request.method=='POST':
        pro.delete()
        return redirect('enquiry')
    params = {
        'item': pro
    }
    return render(request , 'basic/deleteEnquiry.html' , params )


@login_required(login_url='loginPage')
def product(request):
    enq = Product.objects.all()
    form = EnquiryForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else :
            return HttpResponse('<h3> Try again </h3>')
    else :
        form = ProductForm()
    params = {
        'form' : form ,
        'pro' : enq
    }

    return render(request , 'basic/product.html' , params)
    

@login_required(login_url='loginPage')
def productEnquiry(request , pk):
    enq = Product.objects.get(id = pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST , instance=enq)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = ProductForm(instance= enq)
    params = {
        'form' : form
    }
    return render(request , 'basic/productForm.html' , params)
@login_required(login_url='loginPage')
def employee(request):
    emp = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else :
            return render(request , 'basic/404.html')
    else:
        form = EmployeForm()
    params = {
        'form': form,
        'pro': emp
    }
    return render(request , 'basic/employee.html' , params)
@login_required(login_url='loginPage')
def employeeUpdate(request , pk):
    enq = Employee.objects.get(id = pk)
    
    if request.method == 'POST':
        form = EmployeForm(request.POST , instance=enq)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = EmployeForm(instance= enq)
    params = {
        'form' : form
    }
    return render(request , 'basic/empForm.html' , params)
@login_required(login_url='loginPage')
def stock(request):
    pro = Product.objects.all()
    params = {
        'stock': pro
    }
    return render(request , 'basic/album.html' , params)
@login_required(login_url='loginPage')
def clients(request):
    cli = Client.objects.all()
    form = NewClient()
    if request.method=='POST':
        form = NewClient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendarapp:calendar')
        else :
            return render(request , 'basic/404.html')
    else : 
        form = NewClient()
        
    params = {
        'pro' : cli,
        'form' : form
    }
    return render(request , 'basic/forms/newClient.html' , params)

def clientUpdate(request , pk):
    enq = Client.objects.get(id = pk)
    
    if request.method == 'POST':
        form = NewClient(request.POST , instance=enq)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = NewClient(instance= enq)
    params = {
        'form' : form
    }
    return render(request , 'basic/forms/updateClient.html' , params)
def deleteClient(request , pk):
    cli = Client.objects.get(id=pk)
    if request.method == 'POST':
        cli.delete()
        return redirect('clients')
    params = {
        'item': cli
    }
    return render(request , 'basic/forms/deleteClient.html' , params)



@login_required(login_url='loginPage')
def deleteEmployee(request , pk):
    Emp = Employee.objects.get(id=pk)
    if request.method == 'POST':
        Emp.delete()
        return redirect('employee')
       
    
    params = {
        'item': Emp
    }

    return render(request, 'basic/deleteEmployee.html' , params)
@login_required(login_url='loginPage')
def deleteProduct(request , pk):
    pro = Product.objects.get(id=pk)
    if request.method=='POST':
        pro.delete()
        return redirect('product')
    params = {
        'item': pro
    }
    return render(request , 'basic/deleteProduct.html' , params)


def serviceSlip(request):
    cli = Slip.objects.all()
    form = NewSlip()
    if request.method=='POST':
        form = NewSlip(request.POST)
        if form.is_valid():
            form.save()
            return redirect('serviceSlip')
        else :
            return render(request , 'basic/404.html')
    else : 
        form = NewSlip()
        
    params = {
        'pro' : cli,
        'form' : form
    }
    return render(request , 'basic/billing.html' , params)

def updateSlip(request , pk):
    slip = Slip.objects.get(id=pk)
    if request.method == 'POST':
        form = NewSlip(request.POST , instance=slip)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = NewSlip(instance= slip)
    params = {
        'form': form,
        'pro' : slip
    }

    return render(request , 'basic/forms/updateSlip.html' , params)

def deleteSlip(request , pk):
    slip = Slip.objects.get(id=pk)
    if request.method == 'POST':
        slip.delete()
        return redirect('calendarapp:calendar')
    params = {
        'item' : slip
    }
    return render(request , 'basic/forms/deleteSlip.html' , params)