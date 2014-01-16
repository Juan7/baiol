from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.

class Product(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),                  
        (2, _('inactive')),                  
    )
                    
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
