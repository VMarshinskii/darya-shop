from django import template
from catalog.models import Product
from shop.models import UserCart
from shop.view import unserialize, serialize
from django.http import Http404
register = template.Library()

@register.inclusion_tag('templatetags/cart.html')
def cart():
    sum = 0
    count_val = 0
    #if "user_cart" in request.session:
    #    user_key = request.session["user_cart"]
    #    try:
    #        user_cart = UserCart.objects.get(user_key=user_key)
    #        products = unserialize(user_cart.products)
    #        for id, count in products:
    #            try:
    #                pr = Product.objects.get(id=int(id))
    #                sum += pr.price * int(count)
    #                count_val += int(count)
    #            except Product.DoesNotExist:
    #                pass
    #   except UserCart.DoesNotExist:
    #       pass
    return {'sum': sum, 'count': count_val}