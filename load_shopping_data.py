from random import randint, choice
from shop.models import Cart, Order, OrderItem, Rating
from home.models import User
from shop.models import Plant, PlantInventory

def clean_and_populate_data():
    # Clean existing data
    print("Cleaning existing data...")
    Rating.objects.all().delete()
    Cart.objects.all().delete()
    OrderItem.objects.all().delete()
    Order.objects.all().delete()
    print("Existing data cleaned.")

    # Get all users, plants, and inventories
    users = User.objects.all()
    plants = Plant.objects.all()
    inventories = PlantInventory.objects.all()

    # Populate dummy ratings
    print("Populating ratings...")
    for user in users:
        for plant in plants:
            if not Rating.objects.filter(user=user, plant=plant).exists():  # Avoid duplicates
                Rating.objects.create(
                    user=user,
                    plant=plant,
                    rating=randint(1, 5),  # Random rating between 1 and 5
                )

    # Populate dummy carts
    print("Populating carts...")
    for user in users:
        for _ in range(randint(1, 3)):  # Each user gets 1-3 cart items
            plant = choice(plants)
            if not Cart.objects.filter(user=user, plant=plant).exists():  # Avoid duplicates
                Cart.objects.create(
                    user=user,
                    plant=plant,
                    quantity=randint(1, 5),  # Random quantity between 1 and 5
                )

    # Populate dummy orders
    print("Populating orders...")
    for user in users:
        for _ in range(randint(1, 3)):  # Each user gets 1-3 orders
            order = Order.objects.create(
                user=user,
                status=choice(['PENDING', 'PROCESSING', 'SHIPPED', 'DELIVERED']),
                total_price=0,  # Placeholder; will calculate below
            )
            total_price = 0
            for _ in range(randint(1, 5)):  # Each order gets 1-5 items
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
            order.total_price = round(total_price, 2)  # Update total price
            order.save()

    print("Dummy data populated successfully!")

# Run the script
clean_and_populate_data()
