from django.db import models

# Create your models here.
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    class Meta:
        verbose_name="Category"
    def __str__(self):
        return  self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    desc = models.TextField()
    img = models.ImageField(upload_to='uploads/items', blank=True)
