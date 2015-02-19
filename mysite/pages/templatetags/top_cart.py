from django import template
from pages.models import Page
register = template.Library()

@register.inclusion_tag('templatetags/top_cart.html')
def top_cart():
    sum = 0
    count_val = 0
    # user_key = request.session['user_key']
    # try:
    #     user_cart = UserCart.objects.get(user_key=user_key)
    #     products = unserialize(user_cart.products)
    #     for id, count in products:
    #         try:
    #             pr = Product.objects.get(id=int(id))
    #             sum += pr.price * int(count)
    #             count_val += int(count)
    #         except Product.DoesNotExist:
    #             pass
    # except UserCart.DoesNotExist:
    #     pass
    return {'sum': sum, 'count': count_val}