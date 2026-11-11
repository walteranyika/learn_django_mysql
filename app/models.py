import os
import uuid

from django.db import models

def unique_image_path(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    new_filename = f"{uuid.uuid4().hex}{ext}"
    return os.path.join("cover_images", new_filename)

class Author(models.Model):
    names = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.names
    class Meta:
        db_table = 'authors'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    year = models.IntegerField()
    cost = models.IntegerField(default=250)
    cover = models.ImageField(upload_to=unique_image_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


#
# # Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     cost = models.DecimalField(max_digits=10, decimal_places=2)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         db_table = 'products'
#
# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
#     quantity = models.DecimalField(max_digits=10, decimal_places=2)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.product.name
#     class Meta:
#         db_table = 'orders'