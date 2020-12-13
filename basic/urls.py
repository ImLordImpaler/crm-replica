from django.urls import path , include
from . import views
urlpatterns = [
    
    path('dashboard' , views.home , name='dashboard'),
    path('' , views.cover , name='cover'),
    path('product'  ,views.product , name='product'),
    path('enquiry' , views.enquiry , name='enquiry'),
    path('employee'  , views.employee , name='employee'),
    path('stock' , views.stock , name='stock'),
    path('clients' , views.clients , name='clients'),
    path('serviceSlip' , views.serviceSlip , name='serviceSlip'),
    path('followup' , views.followup , name='followup'),
    path('profile' , views.profilePage , name='profile'),
    path('service' , views.service , name='service'),
    path('reports' , views.reports, name='reports'),
   
    
    # update
    path('enquiry/<str:pk>/', views.enquiryUpdate , name = 'enquiryUpdate'),
    path('product/<str:pk>/' , views.productEnquiry , name='productEnquiry'),
    path('employee/<str:pk>/' , views.employeeUpdate , name = 'employeeUpdate'),
    path('client/<str:pk>/' , views.clientUpdate , name='clientUpdate'),
    path('serviceSlip/<str:pk>/' , views.updateSlip , name='updateSlip'),

    #delete 
    
    path('deleteEmployee/<str:pk>/', views.deleteEmployee , name = 'deleteEmployee'),
    path('deleteProduct/<str:pk>/', views.deleteProduct , name = 'productDelete'),
    path('deleteEnquiry/<str:pk>/', views.deleteEnquiry , name = 'enquiryDelete'),
    path('deleteClient/<str:pk>/', views.deleteClient , name = 'clientDelete'),
    path('deleteSlip/<str:pk>/' , views.deleteSlip , name='deleteSlip'),
    #auth
    path('login' , views.loginPage , name='loginPage'),
    path('register' , views.register , name='register'),
    path('logout' , views.logoutPage , name='logoutPage')
   
    

]