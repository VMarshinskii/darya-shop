# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import Http404
from shop.models import UserCart, TypeDelivery
from catalog.models import Product
from forms import OrderForm
import random
import string


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


def return_cart(request):
    sum = 0
    count_all = 0
    products = []
    if "user_cart" in request.session:
        user_key = request.session["user_cart"]
        try:
            user_cart = UserCart.objects.get(user_key=user_key)
            for product_id, count in unserialize(user_cart.products).items():
                try:
                    pr = Product.objects.get(id=product_id)
                    pr.price_new = (pr.price / 100) * (100 - pr.sale)
                    pr.price_sum_new = pr.price_new * int(count)
                    pr.price_sum_old = pr.price * int(count)
                    pr.count = int(count)
                    products.append(pr)
                    count_all += int(count)
                    sum += pr.price_new * int(count)
                except Product.DoesNotExist:
                    pass
        except UserCart.DoesNotExist:
            pass
    return {'count': count_all, 'sum': sum, 'products': products}


def cart(request):
    cart_mass = return_cart(request)
    return render_to_response("cart.html", {'products': cart_mass['products'], 'sum': cart_mass['sum']})


def order(request):
    args = {}
    args.update(csrf(request))
    cart_mass = return_cart(request)
    args['types_delivery'] = TypeDelivery.objects.all()
    args['sum'] = cart_mass['sum']
    args['form'] = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.post)
        form.type_delivery = TypeDelivery.objects.get(id=int(form.cleaned_data['type_delivery']))
        if form.is_valid():
            return render_to_response("order.html", args)
        else:
            args['form'] = form
    return render_to_response("order.html", args)


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
    cart_mass = return_cart(request)
    if 'cart' in request.GET:
        return render_to_response("cart_ajax.html", {'products': cart_mass['products'], 'sum': cart_mass['sum']})
    return render_to_response("add_in_cart.html", {'count': cart_mass['count'], 'sum': cart_mass['sum']})


def del_in_cart(request, id=-1):
    if "user_cart" in request.session:
        user_key = request.session["user_cart"]
        try:
            user_cart = UserCart.objects.get(user_key=user_key)
        except UserCart.DoesNotExist:
            user_cart = UserCart()
            user_cart.user_key = user_key
        products = unserialize(user_cart.products)
        if int(id) in products and products[int(id)] > 0:
            products[int(id)] -= 1
            if products[int(id)] == 0:
                products.pop(int(id))
            user_cart.products = serialize(products)
            user_cart.save()
    cart_mass = return_cart(request)
    return render_to_response("cart_ajax.html", {'products': cart_mass['products'], 'sum': cart_mass['sum']})


def remove_in_cart(request, id=-1):
    if "user_cart" in request.session:
        user_key = request.session["user_cart"]
        try:
            user_cart = UserCart.objects.get(user_key=user_key)
        except UserCart.DoesNotExist:
            user_cart = UserCart()
            user_cart.user_key = user_key
        products = unserialize(user_cart.products)
        products.pop(int(id))
        user_cart.products = serialize(products)
        user_cart.save()
    cart_mass = return_cart(request)
    return render_to_response("cart_ajax.html", {'products': cart_mass['products'], 'sum': cart_mass['sum']})


def cart_top_ajax(request):
    cart_mass = return_cart(request)
    return render_to_response("cart_top_ajax.html", {'count': cart_mass['count'], 'sum': cart_mass['sum']})