# -*- coding: utf-8 -*-
from string import maketrans
from accounts.models import User
from models import Order, TypeDelivery, UserCart
from forms import OrderForm
from catalog.models import Product
from django import forms
import random
import string


def translit(locallangstring):
    conversion = {
        u'\u0410' : 'A',    u'\u0430' : 'a',
        u'\u0411' : 'B',    u'\u0431' : 'b',
        u'\u0412' : 'V',    u'\u0432' : 'v',
        u'\u0413' : 'G',    u'\u0433' : 'g',
        u'\u0414' : 'D',    u'\u0434' : 'd',
        u'\u0415' : 'E',    u'\u0435' : 'e',
        u'\u0401' : 'Yo',   u'\u0451' : 'yo',
        u'\u0416' : 'Zh',   u'\u0436' : 'zh',
        u'\u0417' : 'Z',    u'\u0437' : 'z',
        u'\u0418' : 'I',    u'\u0438' : 'i',
        u'\u0419' : 'Y',    u'\u0439' : 'y',
        u'\u041a' : 'K',    u'\u043a' : 'k',
        u'\u041b' : 'L',    u'\u043b' : 'l',
        u'\u041c' : 'M',    u'\u043c' : 'm',
        u'\u041d' : 'N',    u'\u043d' : 'n',
        u'\u041e' : 'O',    u'\u043e' : 'o',
        u'\u041f' : 'P',    u'\u043f' : 'p',
        u'\u0420' : 'R',    u'\u0440' : 'r',
        u'\u0421' : 'S',    u'\u0441' : 's',
        u'\u0422' : 'T',    u'\u0442' : 't',
        u'\u0423' : 'U',    u'\u0443' : 'u',
        u'\u0424' : 'F',    u'\u0444' : 'f',
        u'\u0425' : 'H',    u'\u0445' : 'h',
        u'\u0426' : 'Ts',   u'\u0446' : 'ts',
        u'\u0427' : 'Ch',   u'\u0447' : 'ch',
        u'\u0428' : 'Sh',   u'\u0448' : 'sh',
        u'\u0429' : 'Sch',  u'\u0449' : 'sch',
        u'\u042a' : '"',    u'\u044a' : '"',
        u'\u042b' : 'Y',    u'\u044b' : 'y',
        u'\u042c' : '\'',   u'\u044c' : '\'',
        u'\u042d' : 'E',    u'\u044d' : 'e',
        u'\u042e' : 'Yu',   u'\u044e' : 'yu',
        u'\u042f' : 'Ya',   u'\u044f' : 'ya',
    }
    translitstring = []
    for c in locallangstring:
        translitstring.append(conversion.setdefault(c, c))
    return ''.join(translitstring)


def random_str(n):
    return "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(n))


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


def unserialize_get(str):
    products = {}
    if str == '':
        return products
    for i in str.split(";"):
        if i != '':
            mass_str = i.split(":")
        try:
            products[Product.objects.get(id=int(mass_str[0]))] = int(mass_str[1])
        except Product.DoesNotExist:
            pass
    return products


def create_username(first_name):
    return translit(first_name) + '_' + random_str(3)


def update_user(request):
    try:
        form = OrderForm(request.POST).save(commit=False)
        user = request.user
        user.phone = form.phone
        user.first_name = form.name
        user.last_name = form.surname
        user.email = form.mail
        user.region = form.region
        user.city = form.city
        user.address2 = form.address
        user.index = form.index
        user.save()
    except User.IntegrityError:
        return None
    return user


def create_user(request, password):
    form = OrderForm(request.POST).save(commit=False)
    user1 = User.objects.filter(phone=form.phone)
    user2 = User.objects.filter(email=form.mail)
    if user1 or user2:
        raise forms.ValidationError("Ошибка")
    user = User()
    user.username = create_username(form.name)
    user.set_password(password)
    user.phone = form.phone
    user.first_name = form.name
    user.last_name = form.surname
    user.email = form.mail
    user.region = form.region
    user.city = form.city
    user.address2 = form.address
    user.index = form.index
    user.save()
    return user


def create_order(request, user):
    form = OrderForm(request.POST)
    ord = form.save(commit=False)
    ord.type_delivery = TypeDelivery.objects.get(id=int(request.POST.get('type_delivery', 0)))
    ord.status = '0'
    ord.sum = ord.type_delivery.price
    user_key = request.session["user_cart"]
    products_str = ''
    try:
        user_cart = UserCart.objects.get(user_key=user_key)
        for product_id, count in unserialize(user_cart.products).items():
            pr = Product.objects.get(id=product_id)
            price = pr.price
            if pr.sale_status == 1:
                price = (pr.price / 100) * (100 - pr.sale)
            ord.sum += price * count
            products_str += pr.image + ";" + pr.name + ";" + str(price) + ";" + str(count) + ";" + str(count*price) + "=="
    except UserCart.DoesNotExist, Product.DoesNotExist:
        pass
    ord.products = products_str
    ord.user = user
    ord.save()
    return ord


def get_model_order(request):
    model = Order()
    model.name = request.user.first_name
    model.surname = request.user.last_name
    model.phone = request.user.phone
    model.mail = request.user.email
    model.region = request.user.region
    model.city = request.user.city
    model.index = request.user.index
    model.address = request.user.address2
    return model