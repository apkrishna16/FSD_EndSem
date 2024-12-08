import random
from shop.models import Plant, PlantInventory  # Replace 'your_app' with your app name

# List of some dummy price ranges and stock ranges
price_range = (5, 50)  # Prices between $5 and $50
stock_range = (0, 100)  # Stock between 0 and 100

# Loop over each plant in the Plant model
for plant in Plant.objects.all():
    # Generate random price and stock quantity for each plant
    price = round(random.uniform(price_range[0], price_range[1]), 2)  # Random price with 2 decimal places
    stock = random.randint(stock_range[0], stock_range[1])  # Random stock quantity
    
    # Create a new PlantInventory entry
    plant_inventory = PlantInventory.objects.create(
        plant=plant,       # Associate with the current plant
        price=price,       # Set the generated price
        stock=stock        # Set the generated stock quantity
    )
    
    # Print confirmation
    print(f"Added {plant_inventory} to PlantInventory")
