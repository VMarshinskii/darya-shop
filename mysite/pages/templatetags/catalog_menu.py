from django import template
from catalog.models import Category
register = template.Library()

@register.inclusion_tag('templatetags/catalog_menu.html')
def catalog_menu():
    parents = Category.objects.filter(parent=None)
    mass_categ = {}
    for cat in parents:
        mass_categ[cat] = {}
        childrens = Category.objects.filter(parent=cat)
        for child in childrens:
            mass_categ[cat].append(child)
    return {'mass_categ': mass_categ}