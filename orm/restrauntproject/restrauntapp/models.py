from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255)

    class Meta:
        db_table = 'restaurants'

    def __str__(self):
        return f"\nID: {self.restaurant_id}\nName{self.name}\nEmail: {self.email}\nCity: {self.city}\n"

class Chef(models.Model):
    chef_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)

    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = 'chefs'

    def __str__(self):
        return f"\nID: {self.chef_id}\nName: {self.name}\nEmail: {self.email}\nRestaurant: {self.restaurant}"

class Cook(models.Model):
    cook_id  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cooks'

    def __str__(self):
        return f"\nID: {self.cook_id}\nName: {self.name}\nEmail: {self.email}\nRestaurant: {self.restaurant}"

class Waiter(models.Model):
    waiter_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = 'waiters'

    def __str__(self):
        return f"\nID: {self.waiter_id}\nName: {self.name}\nEmail: {self.email}\nRestaurant: {self.restaurant}"

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    bio = models.TextField()

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return f"\nID: {self.customer_id}\nName: {self.name}\nEmail: {self.email}"
