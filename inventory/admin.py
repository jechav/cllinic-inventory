from django.contrib import admin
from .models import Product, Location, Brand, Manufacture, Accessory 


class productAdmin(admin.ModelAdmin):
    list_display = (
            'name', 'model', 'series', 'voltage',
            'property', 
    )

    #list_filter = ('load',)

    search_fields = (
            #'tag','activation_date', 'expriry_date',
    )
# Register your models here.
admin.site.register(Product, productAdmin)
admin.site.register(Location)
admin.site.register(Brand)
admin.site.register(Manufacture)
admin.site.register(Accessory)

