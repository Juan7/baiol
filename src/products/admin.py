from django.contrib import admin
from products.models import Product, Category, Department
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
            'fields': ('name', 'department', 'status')
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
