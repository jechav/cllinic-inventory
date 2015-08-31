from django.contrib import admin
from .models import Product, Location, Brand, Manufacture, Accessory 

# Register your models here.
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Brand)
admin.site.register(Manufacture)
admin.site.register(Accessory)

