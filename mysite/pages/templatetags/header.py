from django import template
from accounts.models import SiteSettings
register = template.Library()

@register.inclusion_tag('templatetags/header.html')
def header_show():
    model = SiteSettings.objects.get(id=1)
    return {'model': model}