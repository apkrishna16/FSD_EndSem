from django.urls import path
from . import views

urlpatterns = [
    path('', views.library, name='library'),
    path('plant_info/<int:pk>', views.plant_info, name='plant_info'),
]