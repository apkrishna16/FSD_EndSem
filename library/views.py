from django.shortcuts import render, get_object_or_404
from .models import PlantLibrary

def library(request):
    plants = PlantLibrary.objects.all()
    return render(request, 'library_page.html', {'plants': plants})

def plant_info(request, pk):
    plant_info = get_object_or_404(PlantLibrary, pk=pk) 
    return render(request, 'plant_info.html', {'plant_info': plant_info})
