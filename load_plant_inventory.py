import random
from shop.models import Plant, PlantInventory   
 
price_range = (5, 50)   
stock_range = (0, 100)  
 
for plant in Plant.objects.all():
    # Generate random price and stock quantity for each plant
    price = round(random.uniform(price_range[0], price_range[1]), 2)   
    stock = random.randint(stock_range[0], stock_range[1])   
    
    plant_inventory = PlantInventory.objects.create(
        plant=plant,        
        price=price,        
        stock=stock         
    )
     
    print(f"Added {plant_inventory} to PlantInventory")
