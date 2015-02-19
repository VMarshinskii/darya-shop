# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from shop.models import UserCart
from catalog.models import Product
import random
import string


# Create your views here.
def cart(request):
    products = {}
    sum_mass = {}
    sum = 0
    if "user_cart" in request.session:
        user_key = request.session["user_cart"]
        try:
            user_cart = UserCart.objects.get(user_key=user_key)
            for product_id, count in unserialize(user_cart.products).items():
                try:
                    pr = Product.objects.get(id=product_id)
                    pr.price_sum = pr.price * int(count)
                    products[pr] = count
                    sum += pr.price * int(count)
                except Product.DoesNotExist:
                    pass
        except UserCart.DoesNotExist:
            pass
    return render_to_response("cart.html", {'products': products, 'sum_mass': sum_mass, 'sum': sum})


def order(request):
    return render_to_response("order.html")


def add_in_cart(request, id=-1):
    if "user_cart" in request.session:
        user_key = request.session["user_cart"]
        try:
            user_cart = UserCart.objects.get(user_key=user_key)
        except UserCart.DoesNotExist:
            user_cart = UserCart()
            user_cart.user_key = user_key
        products = unserialize(user_cart.products)
        products[int(id)] = products.get(int(id), 0) + 1
        user_cart.products = serialize(products)
        user_cart.save()
    else:
        user_cart = UserCart()
        user_cart.user_key = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))
        user_cart.products = str(id) + ":1"
        request.session["user_cart"] = user_cart.user_key
        user_cart.save()
    product = Product.objects.get(id=id)
    return render_to_response("add_in_cart.html", {'product': product})


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