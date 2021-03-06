# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import Http404
from shop.models import UserCart, TypeDelivery, Order, Clients
from catalog.models import Product
from accounts.models import Address, User
from additions import create_order, get_model_order, create_user, serialize, unserialize, update_user, random_str, sms
from forms import OrderForm, MailSenderForm
import random
import string
import xlrd


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
                    if pr.sale_status == 1:
                        pr.price_new = (pr.price / 100) * (100 - pr.sale)
                    else:
                        pr.price_new = pr.price
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

    if request.user.is_authenticated():
        if request.POST:
            form = OrderForm(request.POST)
            if form.is_valid():
                ord = create_order(request, request.user)
                user = update_user(request)
                # отправка на e-mail и sms
                phone = user.phone.replace("(", "")
                phone = phone.replace(")", "")
                phone = phone.replace(" ", "")
                phone = phone.replace("-", "")
                sms(phone, "Darya-Shop: Ваш заказ оформлен")
                return render_to_response("order_thanks.html")
            else:
                args['form'] = form
                return render_to_response("order_registered.html", args)
        model = get_model_order(request)
        args['form'] = OrderForm(instance=model)
        args['user'] = request.user
        return render_to_response("order_registered.html", args)

    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            password = random_str(7)
            user = create_user(request, password)
            if user:
                ord = create_order(request, user)
                # отправка на e-mail и sms
                phone = user.phone.replace("(", "")
                phone = phone.replace(")", "")
                phone = phone.replace(" ", "")
                phone = phone.replace("-", "")
                message = "Darya-Shop. Ваш заказ оформлен! Данные для входа в личный кабинет: \nлогин: %s \nпароль: %s" % (
                    phone.encode('utf-8'), password.encode('utf-8'))
                sms(phone, message)
                return render_to_response("order_thanks.html", {'ord': ord, 'password': password})
            else:
                args['error'] = "Вы уже зарегистрированны - войдите в систему"
                args['form'] = form
        else:
            args['form'] = form
        return render_to_response("order_not_registered.html", args)

    return render_to_response("order_not_registered.html", args)


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
        user_cart.user_key = "".join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))
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


def admin_email(request):
    if request.user.is_authenticated():
        args = {}
        args.update(csrf(request))
        args['form'] = MailSenderForm()
        if request.POST:
            form = MailSenderForm(request.POST)
            if form.is_valid():
                clients = Clients.objects.all()
                clients_mails = []
                for client in clients:
                    clients_mails.append(client.mail)
                subject, from_email, to = request.POST.get('theme'), 'from@example.com', ['marshinskii@gmail.com']
                text_content = request.POST.get('text')
                html_content = request.POST.get('text')
                msg = EmailMultiAlternatives(subject, text_content, from_email, clients_mails)
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                pass
            else:
                args['form'] = MailSenderForm(request.POST)
        return render_to_response("admin_email.html", args)
    else:
        return redirect('/admin/')