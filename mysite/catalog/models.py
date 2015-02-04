# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    parent = models.ForeignKey("self", verbose_name="Родительская категория")


class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    price = models.IntegerField("Цена")
    category = models.ForeignKey(Category, verbose_name="Категория", blank=True, null=True)
    sale = models.IntegerField("Скидка, %")
    sale_status = models.IntegerField("Сделать скидку", default=0)
    count_status = models.IntegerField("Под заказ", default=0)
    count = models.IntegerField("Товар в наличии")
    status = models.IntegerField("Рекламные метки", default=0)
    text = models.TextField("Описание")
    keywords = models.CharField("Ключевые слова", max_length=200)
    description = models.CharField("Description", max_length=200)
    images = models.TextField(blank=True)
    image = models.CharField(max_length=200, blank=True)
    related_products = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name