from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
# Create your models here.

class UserProfile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(
        _('avatar'), upload_to='accounts/img/avatar',
        default='accounts/img/avatar/noavatar.jpg'
    )
    user = models.OneToOneField(User)

    def get_display_name(self):
        if self.user.get_full_name() != '':
            return self.user.get_full_name()
        return self.user.username

User.profile = property(lambda s: UserProfile.objects.get_or_create(user=s)[0])
