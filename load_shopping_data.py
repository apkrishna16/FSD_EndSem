from random import randint, choice
from shop.models import Cart, Order, OrderItem, Rating
from home.models import User
from shop.models import Plant, PlantInventory

def clean_and_populate_data(): 
    print("Cleaning existing data...")
    Rating.objects.all().delete()
    Cart.objects.all().delete()
    OrderItem.objects.all().delete()
    Order.objects.all().delete()
    print("Existing data cleaned.")
 
    users = User.objects.all()
    plants = Plant.objects.all()
    inventories = PlantInventory.objects.all()
 
    print("Populating ratings...")
    for user in users:
        for plant in plants:
            if not Rating.objects.filter(user=user, plant=plant).exists():  
                Rating.objects.create(
                    user=user,
                    plant=plant,
                    rating=randint(1, 5),   
                )
 
    print("Populating carts...")
    for user in users:
        for _ in range(randint(1, 3)):   
            plant = choice(plants)
            if not Cart.objects.filter(user=user, plant=plant).exists():   
                Cart.objects.create(
                    user=user,
                    plant=plant,
                    quantity=randint(1, 5),   
                )

  
    print("Populating orders...")
    for user in users:
        for _ in range(randint(1, 3)):  
            order = Order.objects.create(
                user=user,
                status=choice(['PENDING', 'PROCESSING', 'SHIPPED', 'DELIVERED']),
                total_price=0,   
            )
            total_price = 0
            for _ in range(randint(1, 5)):   
                inventory = choice(inventories)
                quantity = randint(1, 5)
                price = inventory.price * quantity
                OrderItem.objects.create(
                    order=order,
                    plant=inventory.plant,
                    quantity=quantity,
                    price=price,
                )
                total_price += price
            order.total_price = round(total_price, 2)   
            order.save()

    print("Dummy data populated successfully!")
 
clean_and_populate_data()
