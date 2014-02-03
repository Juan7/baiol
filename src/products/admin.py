from django.contrib import admin
from products.models import Product, Category, Department, ProductInstance, Variation
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'status',)
    #prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'description', 'avatar', 'status')
        }),
        ('Meta', {
            'fields': ('updated_at', 'created_at')
        }),
    )
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status',)
    #prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'department', 'category', 'status')
        }),
        ('Meta', {
            'fields': ('updated_at', 'created_at')
        }),
    )
admin.site.register(Category, CategoryAdmin)

class DepartmentAdmin(admin.ModelAdmin):
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
admin.site.register(Department, DepartmentAdmin)

class ProductInstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status',)
    #prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'product', 'variation', 'status')
        }),
        ('Meta', {
            'fields': ('updated_at', 'created_at')
        }),
    )
admin.site.register(ProductInstance, ProductInstanceAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'status',)
    #prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('key', 'value',  'status')
        }),
        ('Meta', {
            'fields': ('updated_at', 'created_at')
        }),
    )
admin.site.register(Variation, VariationAdmin)
