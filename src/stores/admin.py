from django.contrib import admin
from stores.models import Store, StoreProduct
# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'status',)
    prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'avatar', 'banner', 'status')
        }),
        ('Meta', {
            'fields': ('updated_at', 'created_at')
        }),
    )
    
admin.site.register(Store, StoreAdmin)

class StoreProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'store', 'product', 'status')
    #prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'store', 'product', 'status')
        }),
        ('Meta', {
            'fields': ('updated_at', 'created_at')
        }),
    )

admin.site.register(StoreProduct, StoreProductAdmin)
