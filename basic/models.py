from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import Client



class Customer(models.Model):
    name= models.CharField(max_length=100 , null=True , blank=True)
    age = models.IntegerField(default=10)
    phone = models.CharField(max_length=10 , blank=True , null=True)
    root = models.OneToOneField(User , on_delete=models.CASCADE)
    dob = models.DateField(null=True , blank=True)
    def __str__(self):
        return self.root.username
@receiver(post_save , sender=User)
def update_user_profile(sender , instance , created , **kwargs):
    if created: 
        Customer.objects.create(root=instance)
    instance.customer.save()

# Services LIST OF SERVICES
GENDER_TYPES = [
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others') 
    ]

class Service(models.Model):
    name = models.CharField(max_length=100 , null=True ,blank=True)
    price = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    mprice = models.IntegerField(default=0)
    gender = models.CharField(max_length=10 , choices=GENDER_TYPES , default='others')
    def __str__(self):
        return (self.name + ' (' + self.gender + ' )')


#LIST OF CATEGORIES


class Category(models.Model):
    name = models.CharField(max_length=100 , null=True , blank=True)
    service = models.ForeignKey(Service , on_delete= models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100 ,null=True , blank=True )
    bprice = models.IntegerField(default=0 , null=True  , blank=True)
    sprice = models.IntegerField(default=0 , null= True , blank=True)
    category = models.ForeignKey(Category , on_delete= models.CASCADE)
    quantity = models.IntegerField(default=10)
    img = models.ImageField(null=True , blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


#ENQUIRY

ENQUIRY_TYPE = [
        ('warm', 'warm'),
        ('normal', 'normal'),
        ('cold', 'cold') 
    ]
class Enquiry(models.Model):
    name = models.CharField(max_length=100 , null=True  , blank=True)
    phone = models.CharField(max_length=100 , null=True  , blank=True)
    service = models.ForeignKey(Service , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    responseType = models.CharField(null=True , blank=True , max_length=100)
    response = models.CharField(max_length= 10 , choices=ENQUIRY_TYPE , default='cold')
    

    def __str__(self):
        return self.name

class Employee(models.Model):
    name= models.CharField(max_length=100 , null=True , blank=True)
    age = models.IntegerField(default=18 )
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    phone = models.CharField(max_length=10 , null=True , blank=True)
    email = models.EmailField(max_length=100 , null=True, blank=True)
    def __str__(self):
        return self.name 

from datetime import date
class Client(models.Model):
    name = models.CharField(max_length= 100 , null=True , blank=True)
    email = models.EmailField(max_length=100 , null=True , blank=True)
    phone = models.CharField(max_length=10 , null=True , blank=True)
    address = models.CharField(max_length=500 , null=True , blank=True)
    dob = models.DateField(null=True , blank=True)

    def __str__(self):
        return self.name
    @property
    def is_birthday(self):
        return date.today() == self.dob

class Slip(models.Model):
    name= models.CharField(max_length=100 , null=True , blank=True)
    phone = models.CharField(max_length=10 , null=True )
    client = models.ForeignKey(Client , on_delete = models.CASCADE  , null=True , blank=True)
    service = models.ManyToManyField(Service , default=None)
    product = models.ManyToManyField(Product , default = None)
    emp = models.ForeignKey(Employee , on_delete = models.CASCADE)
    time = models.TimeField(auto_now=True)
    
  
    def __str__(self):
        return self.emp.name


class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return self.result
    
    def save(self , *args , **kwargs):
        account_sid = 'ACb91a2c25619fb9721624295f0c5ce90e'
        auth_token = '6ee2015415e19ec8b9f7b7a9ab17d92b'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_='+2566676184',
                        to='+8178073305'
                    )
        
    






