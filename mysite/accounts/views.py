# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponseRedirect, redirect
from django.core.context_processors import csrf
from django.http import Http404
from django.contrib import auth
from shop.additions import unserialize_get, translit, random_str
from shop.models import Order
from forms import LoginForm, UserRegistrationForm, SiteSettingsForm
from models import User, SiteSettings
from catalog.models import Product


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
            password = random_str(6)
            us = form.save(commit=False)
            us.username = translit(us.first_name) + '_' + random_str(3)
            us.set_password(password)
            us.save()
            return render_to_response("registration_thank.html", {'username': us.phone, 'password': password})
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
            mass_pr = order.products.split("==")
            mass_pr_new = []
            for prr in mass_pr:
                if prr != '':
                    new_pr = Product()
                    data = prr.split(";")
                    new_pr.image = data[0]
                    new_pr.name = data[1]
                    new_pr.price = data[2]
                    new_pr.count = data[3]
                    new_pr.price_all = data[4]
                    mass_pr_new.append(new_pr)
            order.products = mass_pr_new
            order.status = status_mass[order.status]
        orders = reversed(orders)
        return render_to_response("my_orders.html", {'orders': orders})
    return render_to_response("my_orders_not_registered.html")


def my_order(request, id=-1):
    if request.user.is_authenticated():
        try:
            order = Order.objects.get(id=id)
            if request.user == order.user:
                mass_pr = order.products.split("==")
                mass_pr_new = []
                for prr in mass_pr:
                    if prr != '':
                        new_pr = Product()
                        data = prr.split(";")
                        new_pr.image = data[0]
                        new_pr.name = data[1]
                        new_pr.price = data[2]
                        new_pr.count = data[3]
                        new_pr.price_all = data[4]
                        mass_pr_new.append(new_pr)
                order.products = mass_pr_new
                return render_to_response("my_order.html", {'order': order})
        except Order.DoesNotExist:
            pass
    raise Http404("Страница не найдена!")


def admin_settings(request):
    if request.user.is_authenticated():
        args = {}
        args.update(csrf(request))
        try:
            model = SiteSettings.objects.get(id=1)
            args['form'] = SiteSettingsForm(instance=model)
        except SiteSettings.DoesNotExist:
            args['form'] = SiteSettingsForm()

        if request.POST:
            form = SiteSettingsForm(request.POST)
            if form.is_valid():
                model = form.save(commit=False)
                model.id = 1
                model.save()
                return redirect('/admin/')
            else:
                args['form'] = form

        return render_to_response("admin_settings.html", args)
    else:
        return redirect('/admin/')