from django import template
from pages.models import Page
register = template.Library()

@register.inclusion_tag('templatetags/top_cart.html')
def top_cart():
    return {'count': 0, 'sum': 0}