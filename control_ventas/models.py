from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField(default=1)
    cost = models.IntegerField(default=0)
    sell = models.IntegerField(default=0)
    created = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Sells(models.Model):
    day = models.DateField(null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    total_import = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_import = self.product.sell * self.amount
        super().save(*args, **kwargs)
        
class Totalimports(models.Model):
    day = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    
    
