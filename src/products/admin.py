from django.contrib import admin
from products.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'status',)
    #prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'status')
        }),
        ('Meta', {
            'fields': ('updated_at', 'created_at')
        }),
    )
admin.site.register(Product, ProductAdmin)
