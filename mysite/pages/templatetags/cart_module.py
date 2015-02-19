from django import template
from catalog.models import Product
from shop.models import UserCart
from shop.view import unserialize, serialize
from django.http import Http404

register = template.Library()

@register.inclusion_tag('templatetags/cart_module.html')
def cart_module():
    sum = 0
    count_val = 0
    return {'sum': sum, 'count': count_val}