from django.db import models

from django.db import models

class Seller(models.Model):
    name = models.CharField(default='', max_length=200)
    phone = models.CharField(default='', max_length=20)
    address = models.CharField(default='', max_length=400)
    distressed = models.CharField(default = '', max_length= 3)

    web_site = models.URLField(default='', max_length=100)

class House(models.Model):
  address = models.CharField(default='', max_length=200)
  city = models.CharField(default = '', max_length= 100)
  state = models.CharField(default = '', max_length= 2)
  bedrooms = models.CharField(default = '', max_length= 2)
  baths = models.CharField(default = '', max_length= 2)
  garage = models.CharField(default = '', max_length= 3)
  basement = models.CharField(default = '', max_length= 3)
  ac = models.CharField(default = '', max_length= 3)
  forcedheat = models.CharField(default = '', max_length= 3)
  currentrent = models.CharField(default = '', max_length= 10)
  rented = models.CharField(default = '', max_length= 10)
  img_url = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

class Buyer(models.Model):
    name=models.CharField(default='', max_length=100)
    phone=models.TextField(default='')
    company=models.DecimalField(max_digits=10, decimal_places=2)
    specifications=models.DecimalField(max_digits=10, decimal_places=2)
   

    def __str__(self):
        return self.name