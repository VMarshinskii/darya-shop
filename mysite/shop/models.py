# -*- coding: utf-8 -*-
from django.db import models
from accounts.models import User, Address


Order_Status = (
    ('0', 'Обрабатывется'),
    ('1', 'Ждёт оплаты'),
    ('2', 'Оплачен'),
    ('3', 'Отправлен'),
)


class TypeDelivery(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=200)
    price = models.IntegerField("Под заказ", default=0)


class UserCart(models.Model):
    user_key = models.CharField("Ключ", max_length=200)
    products = models.CharField("Товары", max_length=200)


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", blank=True, null=True)
    address = models.ForeignKey(Adderss, verbose_name="Адрес", blank=True, null=True)
    type_delivery = models.ForeignKey(TypeDelivery, verbose_name="Вариант доставки", blank=True, null=True)
    products = models.CharField("Заказ", max_length=200)
    status = models.CharField(max_length=1, choices=Order_Status)
    date_create = models.DateField("Дата создания заказа", auto_now_add=True)
    date_change = models.DateField("Дата редактирования заказа", auto_now=True)
    admin_comment = models.TextField("Комментарий администратора")