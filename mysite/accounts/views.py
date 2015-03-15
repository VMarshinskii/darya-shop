# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from django.http import Http404
from django.contrib import auth
from shop.additions import unserialize_get, translit, random_str
from shop.models import Order
from forms import LoginForm, UserRegistrationForm
from models import User


def ajax_login(request):
    args = {}
    args.update(csrf(request))
    args['form'] = LoginForm()

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                us = User.objects.get(phone=request.POST.get('login'))
                username = us.username
                password = request.POST.get('password')
                user = auth.authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                    return render_to_response("yes.html", {'us': us})
            except User.DoesNotExist:
                pass
        args['form'] = form
        args['error'] = "Данные введены не верно!"
        return render_to_response("ajax_login.html", args)

    return render_to_response("ajax_login.html", args)


def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/")


def registration(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserRegistrationForm()
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            us = form.save(commit=False)
            us.username = translit(us.first_name) + '_' + random_str(3)
            us.password = random_str(6)
            us.save()
            return render_to_response("registration_thank.html")
        args['form'] = form
    return render_to_response("registration.html", args)


def my_orders(request):
    status_mass = {
        '0': 'Обрабатывется',
        '1': 'Ждёт оплаты',
        '2': 'Оплачен',
        '3': 'Отправлен',
    }
    if request.user.is_authenticated():
        orders = Order.objects.filter(user=request.user)
        for order in orders:
            order.products = unserialize_get(order.products)
            order.status = status_mass[order.status]
        return render_to_response("my_orders.html", {'orders': orders})
    return render_to_response("my_orders_not_registered.html")


def my_order(request, id=-1):
    if request.user.is_authenticated():
        try:
            order = Order.objects.get(id=id)
            if request.user == order.user:
                order.products = unserialize_get(order.products)
                return render_to_response("my_order.html", {'order': order})
        except Order.DoesNotExist:
            pass
    raise Http404("Страница не найдена!")