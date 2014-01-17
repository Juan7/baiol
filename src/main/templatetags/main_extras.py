# -*- coding: utf-8 -*-
from django import template
from django.conf import settings

from main.functions import generate_thumbnail

import os

register = template.Library()


@register.filter
def thumbnail(value, arg):
    thumb_size = arg.split('x')
    split = value.name.rsplit('.', 1)
    thumb_path = '%s.%sx%s.%s' % \
        (split[0], thumb_size[0], thumb_size[1], 'jpg')

    if not os.path.exists(settings.MEDIA_ROOT + thumb_path):
        generate_thumbnail(
            value.path, (int(thumb_size[0]), int(thumb_size[1])))
    return thumb_path


@register.filter
def lookup(d, key):
    if key in d:
        return d[key]
    else:
        return None


@register.filter
def make_range(n):
    return list(range(int(n)))
