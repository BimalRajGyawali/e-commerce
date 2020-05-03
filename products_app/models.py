from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

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
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.name



class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)








