from django import template
register = template.Library()

@register.inclusion_tag('templatetags/catalog_menu.html')
def catalog_menu():
    return {'oll_pages': "dfdsfgsdfg"}