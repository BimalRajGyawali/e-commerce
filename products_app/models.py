from django.db import models


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
    stock = models.IntegerField()


    def __str__(self):
        return self.name








