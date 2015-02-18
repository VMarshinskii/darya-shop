# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from shop.models import UserCart


# Create your views here.
def cart(request):
    return render_to_response("cart.html")


def order(request):
    return render_to_response("order.html")


def add_in_cart(request, id=-1):
    if "user_cart" in request.session:
        user_key = request.session["user_cart"]
        try:
            user_cart = UserCart.objects.get(user_key=user_key)
        except UserCart.DoesNotExist:
            user_cart = UserCart()
            user_cart.user_key = "dXs3fFD4sd5g"
        products = unserialize(user_cart.products)
        products[int(id)] = products.get(int(id), 0) + 3
        user_cart.products = serialize(products)
        user_cart.save()
    else:
        request.session["user_cart"] = "dXs3fFD4sd5g"
    return render_to_response("order.html")


def unserialize(str):
    products = {}
    if str == '':
        return products
    for i in str.split(";"):
        if i != '':
            mass_str = i.split(":")
        products[int(mass_str[0])] = int(mass_str[1])
    return products


def serialize(products):
    str_mass = []
    for key, value in products.items():
        str_mass.append(str(key) + ":" + str(value))
    return ";".join(str_mass)