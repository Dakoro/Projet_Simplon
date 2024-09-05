
from django.template.defaulttags import register

@register.filter(name='split_zip')
def split_zip(a, b):
    if isinstance(a, str) and isinstance(b, str):
        split_a = a.split(";")
        split_b = b.split(";")
        return zip(split_a, split_b)