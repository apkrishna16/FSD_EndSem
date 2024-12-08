from django.db import models 

class Plant(models.Model):
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)
    light_requirements = models.CharField(max_length=50)  # Low, Medium, High
    watering_frequency = models.CharField(max_length=50)  # Weekly, Bi-weekly, Monthly
    maintenance_level = models.CharField(max_length=50)  # Low, Medium, High
    growth_rate = models.CharField(max_length=50)  # Slow, Medium, Fast
    preferred_climate = models.CharField(max_length=50)  # Tropical, Arid, etc.
    plant_size = models.CharField(max_length=50)  # Small, Medium, Large
    allergy_concerns = models.BooleanField(default=False)  # Yes/No
    aesthetic_preference = models.CharField(max_length=50)  # Minimalist, Lush, Unique, etc.
    purpose = models.CharField(max_length=100)  # Decorative, Air Purification, etc.
    room_temperature = models.CharField(max_length=50)  # Cold, Cool, Moderate, etc.
    humidity_level = models.CharField(max_length=50)  # Low, Medium, High
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.common_name


class PlantInventory(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='inventory')
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the plant
    stock = models.PositiveIntegerField(default=0)  # Stock of the plant available

    def __str__(self):
        return f"{self.plant.common_name} - {self.price} USD, Stock: {self.stock}"

class Cart(models.Model):
    user = models.ForeignKey('home.User', on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart - {self.plant.common_name}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey('home.User', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username} ({self.status})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order.id} - {self.plant.common_name}"

class Rating(models.Model):
    user = models.ForeignKey('home.User', on_delete=models.CASCADE)  # User who gave the rating
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)  # Plant being rated
    rating = models.PositiveIntegerField()  # Rating value (e.g., 1 to 5 stars)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'plant')  # Ensures one rating per user-plant pair

    def __str__(self):
        return f"{self.user.username} rated {self.plant.common_name} ({self.rating})"