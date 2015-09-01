from django.contrib import admin
from .models import Product, Location, Brand, Manufacture, Accessory 


class productAdmin(admin.ModelAdmin):
    list_display = (
            'name', 'model', 'series', 'voltage',
            'frequency', 'property', 'state', 
            'type', 'location', 'brand', 'manufacture', 
    )

    list_filter = ('property', 'state', 'type',)

    search_fields = (
            'name','series', 'model',
    )
# Register your models here.
admin.site.register(Product, productAdmin)
admin.site.register(Location)
admin.site.register(Brand)
admin.site.register(Manufacture)
admin.site.register(Accessory)

