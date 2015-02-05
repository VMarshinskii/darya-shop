# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    parent = models.ForeignKey("self", verbose_name="Родительская категория", blank=True, null=True)
    url = models.CharField("Url", max_length=200, blank=True)
    description = models.CharField("Description", max_length=200, blank=True)
    keywords = models.CharField("Ключевые слова", max_length=200, blank=True)
    step = models.IntegerField("Вложенность", blank=True, editable=False, default=0)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __unicode__(self):
        return self.title

    def get_all_product(self):
        mass_product = []

        def rec_category(obj):
            product = Product.objects.filter(category=obj)
            for product in product:
                mass_product.append(product)
            categories = Category.objects.filter(parent=obj)
            for category in categories:
                rec_category(category)
        rec_category(self)
        return mass_product

    def get_path_categ(self):
        mass_pass = []

        def rec_path(obj):
            if obj is not None:
                mass_pass.append(obj)
                rec_path(obj)
        rec_path(self)
        return mass_pass


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