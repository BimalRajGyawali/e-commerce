from django.db import models
from django.shortcuts import reverse

# Create your models here.
COLOR = (('violet', 'Violet'), ('green','Green'),('cyan','Cyan'),
         ('orange','Orange'),('red','Red'),('purple','Purple'),('indigo','Indigo'),('pink','Pink'))

class Category(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=20,choices=COLOR)

    class Meta:
        verbose_name = "Categorie"

    def __str__(self):
        return self.title



class Product(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    desc = models.TextField()
    img = models.ImageField(upload_to='uploads/items', blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)


class CardDetails(models.Model):
    number = models.CharField(max_length=20)
    expiry_date = models.CharField(max_length=100)
    cvv = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    ordered_items = models.ManyToManyField(OrderItem)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.name









