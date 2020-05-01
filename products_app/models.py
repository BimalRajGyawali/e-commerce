from django.db import models

<<<<<<< HEAD

=======
# Create your models here.
# Create your models here.
>>>>>>> 148f48595b191e18f935c923669eff9392d33199
class Category(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    class Meta:
<<<<<<< HEAD
        verbose_name = "Categorie"

    def __str__(self):
        return self.title
=======
        verbose_name="Category"
    def __str__(self):
        return  self.name
>>>>>>> 148f48595b191e18f935c923669eff9392d33199


class Product(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
<<<<<<< HEAD
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











=======
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    desc = models.TextField()
    img = models.ImageField(upload_to='uploads/items', blank=True)
>>>>>>> 148f48595b191e18f935c923669eff9392d33199
