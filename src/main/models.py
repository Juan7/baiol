from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.

class Address(models.Model):
    STATUS_CHOICES = (
        (1, _('active')),
        (2, _('inactive')),
    )
    
    description = models.CharField(max_length=255)
    meta = models.CharField(max_length=255, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)