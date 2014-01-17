import unicodedata

from PIL import Image

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def generate_thumbnail(name, thumb_size):
    thumb_w, thumb_h = thumb_size
    split = name.rsplit('.', 1)
    thumb_name = '%s.%sx%s.%s' % (split[0], thumb_w, thumb_h, 'jpg')

    image = Image.open(name)

    if image.mode not in ('L', 'RGB', 'RGBA'):
        image = image.convert('RGB')

    image2 = image
    image2.thumbnail(thumb_size, Image.ANTIALIAS)
    image2.save(thumb_name, "JPEG")


def clean_slug(slug):
    name = slug.lower()
    name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore')
    name = name.replace('-', ' ').replace('_', ' ')
    name = ''.join(c for c in name if c.isalnum() or c == ' ')
    name = '-'.join(name.strip().split())
    name = name[0:100]
    return name


def validate_whitespaces(value):
    if value.strip() == '':
        raise ValidationError(
            _('You must provide more than just whitespaces.'))
