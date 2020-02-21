from django.db import models

class Seller(models.Model):
    name = models.CharField(default='Owners Name', max_length=200)
    phone = models.CharField(default='Owners-Phone-Number', max_length=20)
    address = models.CharField(default='Street, City, State', max_length=100)
    distressed = models.CharField(default = 'If Distressed Please describe', max_length= 400)

class House(models.Model):
    address = models.CharField(default='Rental Address', max_length=200)
    city = models.CharField(default = 'Rental City', max_length= 100)
    state = models.CharField(default = '', max_length= 2)
    bedrooms = models.CharField(default = '', max_length= 2)
    baths = models.CharField(default = '', max_length= 2)
    garage = models.CharField(default = '', max_length= 3)
    basement = models.CharField(default = '', max_length= 3)
    ac = models.CharField(default = '', max_length= 3)
    forcedheat = models.CharField(default = '', max_length= 3)
    currentrent = models.CharField(default = '', max_length= 10)
    rented = models.CharField(default = '', max_length= 10)
    img_url = models.ImageField(upload_to='images/', null=True, blank=True)

class Buyer(models.Model):
    name=models.CharField(default='Buyers Name', max_length=100)
    phone=models.CharField(default='Buyers-Phone-Number', max_length= 100)
    email= models.CharField(default = 'Buyers-email', max_length= 100)
    company= models.CharField(default = 'Buyers-Company Name', max_length= 100)
    specifications= models.CharField(default = 'What are they looking for', max_length= 400)
   
    def __str__(self):
        return self.name