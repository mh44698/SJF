from django import forms
from .models import House, Seller, Buyer

class SellerForm(forms.ModelForm):

    class Meta:
        model = Seller
        fields = ('name','phone', 'address', 'distressed')

class HouseForm(forms.ModelForm):

    class Meta:
        model = House
        fields = ('address', 'city', 'state','bedrooms', 'baths', 'garage', 'basement', 'ac', 'forcedheat', 'currentrent', 'rented','img_url')

class ImageUploadForm(forms.Form):
       image = ('img_url')


class BuyerForm(forms.ModelForm):

    class Meta:
        model = Buyer
        fields = ('name', 'phone', 'email', 'company','specifications')

