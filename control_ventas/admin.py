from django.contrib import admin
from .models import Products, Sells

class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Products, ProductsAdmin)
admin.site.register(Sells)