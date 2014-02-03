from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.

class Department(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),                  
        (2, _('inactive')),                  
    )
    
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),                  
        (2, _('inactive')),                  
    )
    
    name = models.CharField(max_length=255)
    category = models.ManyToManyField('self', blank=True)
    department = models.ManyToManyField(Department, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),                  
        (2, _('inactive')),                  
    )
                    
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    avatar = models.ImageField(_('avatar'), upload_to='products/img/gallery',
        default='products/img/gallery/nopicture.jpg')
    category = models.ManyToManyField(Category)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
   
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
    
    def __str__(self):
        return self.key + ' : ' + self.value
    
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
    
    def __str__(self):
        return self.name
        
class Picture(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),                  
        (2, _('inactive')),                  
    )
    
    image = models.ImageField(_('picture'), upload_to='products/img/gallery',
        default='products/img/gallery/nopicture.jpg')
    product = models.ForeignKey(Product)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    