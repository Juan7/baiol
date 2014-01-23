from django.db import models
from django.utils.translation import ugettext as _

from django.contrib.auth.models import User
from main.models import Address
from products.models import ProductInstance

# Create your models here.

class Store(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),
        (2, _('inactive')),
    )
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(blank=True)
    banner = models.ImageField(blank=True)
    link_color = models.CharField(max_length=10)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class StorePermission(models.Model):
    ROL_CHOICES = (
        (1, _('admin')),
        (2, _('worker')),
        (3, _('client')),
    )
    
    user = models.ForeignKey(User)
    store = models.ForeignKey(Store)
    rol = models.IntegerField(choices=ROL_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class StoreBranch(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),
        (2, _('inactive')),
    )
    
    alias = models.CharField(max_length=255)
    store = models.ForeignKey(Store)
    address = models.ForeignKey(Address)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class StoreProduct(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),
        (2, _('inactive')),
    )
    
    name = models.CharField(max_length=255)
    product = models.ForeignKey(ProductInstance)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)