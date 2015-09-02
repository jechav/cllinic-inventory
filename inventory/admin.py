from django.contrib import admin
from .models import Product, Location, Brand, Manufacture, Accessory, Sublocation 
from actions import export_as_excel


class productAdmin(admin.ModelAdmin):
    list_display = (
            'name', 'model', 'series', 'votage_complete',
            'frequency', 'property', 'state', 
            'type', 'location_complete', 'brand', 'manufacture', 
            'accessories_name',
    )

    def accessories_name(self, obj):
        return ",\n ".join([a.name for a in obj.accessories.all()]) if len(obj.accessories.all()) > 0 else  "Ninguno"
    accessories_name.short_description = "Accesorios"

    def location_complete(self, obj):
        return obj.location.name+" - "+obj.location.service.name
    location_complete.admin_order_field = 'location'
    location_complete.short_description = "Localizacion"

    def votage_complete(self, obj):
        return `obj.voltage`+" "+obj.voltage_type.upper()
    votage_complete.admin_order_field = 'voltage'
    votage_complete.short_description = "Voltaje"

    list_filter = ('property', 'state', 'type',)

    search_fields = (
            'name','series', 'model',
    )
    actions = (export_as_excel, )
# Register your models here.
admin.site.register(Product, productAdmin)
admin.site.register(Sublocation)
admin.site.register(Location)
admin.site.register(Brand)
admin.site.register(Manufacture)
admin.site.register(Accessory)

