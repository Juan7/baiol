from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.

class Product(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),                  
        (2, _('inactive')),                  
    )
                    
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Category(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),                  
        (2, _('inactive')),                  
    )
    
    CATEGORY_CHOICES = (
        (1, _('primary')),                  
        (2, _('secondary')),                  
    )
    
    name = models.CharField(max_length=255)
    parents = models.TextField(blank=True)
    children = models.TextField(blank=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_parents(self):
        parents = self.parents.split(',')
        parents.pop()
        return parents
    
    def get_children(self):
        parents = self.parents.split(',')
        parents.pop()
        return parents

    def is_parent(elem):
        return elem in self.get_parents()
    
    def is_child(elem):
        return elem in self.get_children()

    def save(self, *args, **kwargs):
        #print(self.code)
        if len(self.get_parents()) > 0:
            self.category = 2
        super(Category, self).save(*args, **kwargs)
        
class ProductInstance(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),                  
        (2, _('inactive')),                  
    )
    
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    variation = models.ManyToManyField(Variation)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       
class Variation(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),                  
        (2, _('inactive')),                  
    )
    
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Picture(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),                  
        (2, _('inactive')),                  
    )
    
    image = models.ImageField(blank=True)
    product = models.ForeignKey(Product)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    