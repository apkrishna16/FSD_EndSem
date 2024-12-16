from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant

def shop(request):
    if request.method == 'POST':
        return redirect('cart')
    plants = Plant.objects.prefetch_related('inventory')
    return render(request, 'shop.html', {'plants': plants})

def product_details(request, plant_id):  
    plant_info = get_object_or_404(Plant, id=plant_id) 
    print(plant_info)
    return render(request, 'product_details.html', {'plant_info': plant_info})

def cart(request):    
    return render(request, 'cart.html')