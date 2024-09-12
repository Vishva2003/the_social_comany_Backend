# models.py
from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='sellers/', null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    warranty_offer = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='reviews/images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=0)
    offer_price = models.DecimalField(max_digits=10, decimal_places=0)
    images = models.ImageField(upload_to='products/images/', null=True, blank=True)
    
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    reviews = models.ManyToManyField(Review, blank=True)

    def __str__(self):
        return self.title
