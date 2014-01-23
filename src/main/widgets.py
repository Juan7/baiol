from django import forms
from django.utils.safestring import mark_safe
from main.templatetags.main_extras import thumbnail
from django.conf import settings


class AvatarWidget(forms.FileInput):

    def __init__(self, attrs={}):
        super(AvatarWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        img_path = thumbnail(value, '150x150')
        if value and hasattr(value, "url"):
            output.append((
                '<br/><br/><a target="_blank" href="%s">'
                '<img src="%s%s" class="img-rounded" /></a><br/><br/>'
                          % (value.url, settings.MEDIA_URL, img_path)))
        output.append(super(AvatarWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
