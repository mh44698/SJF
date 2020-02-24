from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseForbidden

def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'seller_list.html', {'sellers': sellers})

def seller_detail(request, id):
    seller = Seller.objects.get(id = id)
    return render(request, 'seller_detail.html', {'seller': seller})

def seller_create(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid:
            seller = form.save()
            return redirect('seller_detail', id = seller.id)
    else:
        form = SellerForm()
        return render(request, 'seller_form.html', {'form': form})

def seller_update(request, id):
    seller = Seller.objects.get(id = id)
    if request.method == 'POST':
        form = SellerForm(request.POST, instance = seller)
        if form.is_valid:
            seller = form.save()
            return redirect('seller_detail', id = seller.id)
    else:
        form = SellerForm(instance = seller)
        return render(request, 'seller_form.html', {'form': form})

def seller_delete(request, id):
    #if request.method == 'POST':
    Seller.objects.get(id = id).delete()
    return redirect('seller_list')


##########################   Buyer 
def buyer_list(request):
    buyers = Buyer.objects.all()
    return render(request, 'buyer_list.html', {'buyers': buyers})

def buyer_detail(request, id):
    buyer = Buyer.objects.get(id = id)
    return render(request, 'buyer_detail.html', {'buyer': buyer})

def buyer_create(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid:
            buyer = form.save()
            return redirect('buyer_detail', id = buyer.id)
    else:
        form = BuyerForm()
        return render(request, 'buyer_form.html', {'form': form})

def buyer_update(request, id):
    buyer = Buyer.objects.get(id = id)
    if request.method == 'POST':
        form = BuyerForm(request.POST, instance = buyer)
        if form.is_valid:
            buyer = form.save()
            return redirect('buyer_detail', id = buyer.id)
    else:
        form = BuyerForm(instance = buyer)
        return render(request, 'buyer_form.html', {'form': form})

def buyer_delete(request, id):
    #if request.method == 'POST':
    Buyer.objects.get(id = id).delete()
    return redirect('buyer_list')

##################  House Views
def house_list(request):
    houses = House.objects.all()
    return render(request, 'house_list.html', {'houses': houses})

def house_detail(request, id):
    house = House.objects.get(id = id)
    return render(request, 'house_detail.html', {'house': house})

def house_create(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid:
            house = form.save()
            return redirect('house_detail', id = house.id)
    else:
        form = HouseForm()
        return render(request, 'house_form.html', {'form': form})

def house_update(request, id):
    house = House.objects.get(id = id)
    if request.method == 'POST':
        form = HouseForm(request.POST, instance = house)
        if form.is_valid:
            house = form.save()
            return redirect('house_detail', id = house.id)
    else:
        form = HouseForm(instance = house)
        return render(request, 'house_form.html', {'form': form})

def house_delete(request, id):
    #if request.method == 'POST':
    House.objects.get(id = id).delete()
    return redirect('house_list')

def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid:
            # buyer = Buyer.objects.get(id=id)
            buyer.img_url = form.cleaned_data['image']
            buyer=form.save()
            # return redirect('buyer_detail', id = buyer.id)
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')

# Create your views here. 
def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
    return render(request, 'hotel_image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 
