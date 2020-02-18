from django.contrib import admin

# Register your models here.
from .models import Buyer, Seller, House

admin.site.register([Buyer, Seller, House])