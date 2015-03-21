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
    description = models.TextField("Описание")
    price = models.IntegerField("Цена", default=0)

    class Meta:
        verbose_name = 'Вариант доставки'
        verbose_name_plural = 'Варианты доставки'

    def __unicode__(self):
        return self.title


class UserCart(models.Model):
    user_key = models.CharField("Ключ", max_length=200)
    products = models.CharField("Товары", max_length=200)


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", blank=True, null=True)
    type_delivery = models.ForeignKey(TypeDelivery, verbose_name="Вариант доставки", null=True)
    products = models.CharField("Заказ", max_length=200)
    status = models.CharField("Статус", max_length=1, choices=Order_Status)
    date_create = models.DateField(verbose_name="Дата создания заказа", auto_now_add=True)
    date_change = models.DateField(verbose_name="Дата редактирования заказа", auto_now=True)
    admin_comment = models.TextField(verbose_name="Комментарий администратора", blank=True)
    sum = models.IntegerField("Сумма заказа", default=0)

    name = models.CharField("Имя", max_length=200)
    surname = models.CharField("Фамилия", max_length=200)
    phone = models.CharField("Телефон", max_length=200)
    mail = models.CharField("Имя", max_length=200)

    region = models.CharField("Область", max_length=200)
    city = models.CharField("Город", max_length=200)
    index = models.CharField("Индекс", max_length=200)
    address = models.CharField("Адрес", max_length=200)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __unicode__(self):
        return self.date_create.strftime('%d-%m-%y') + '(' + self.name + ' ' + self.surname + ')'

    def order_title(self):
        return '<a href="#">' + self.name + ' ' + self.surname + '</a>'
    order_title.allow_tags = True

    def order_date(self):
        return self.date_create.strftime('%d-%m-%y')