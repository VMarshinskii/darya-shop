# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField

class Entry(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    short_text = RedactorField(verbose_name=u'Text')


# Create your models here.
class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    price = models.IntegerField("Цена")
    sale = models.IntegerField("Скидка, %")
    sale_status = models.IntegerField("Сделать скидку")
    #count_status = models.IntegerField("Под заказ")
    count = models.IntegerField("Товар в наличии")
    status = models.IntegerField("Рекламные метки")
    text = models.TextField("Описание")
    keywords = models.CharField("Ключевые слова", max_length=200)
    description = models.CharField("Description", max_length=200)

    def __unicode__(self):
        return self.name
