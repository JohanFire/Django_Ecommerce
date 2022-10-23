from django.db import models
from category.models import Category

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # ([relation with 'Category'], delete products related to this category)
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.product_name + ": " + self.category