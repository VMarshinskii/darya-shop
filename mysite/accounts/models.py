# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Модифицируем поле email.
# _meta это экземпляр django.db.models.options.Options, который хранит данные о модели.
# Это немного хак, но я пока не нашел более простого способа переопределить поле из базовой модели.
AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False


class User(AbstractUser):
    # Добавляем поля аватара. null=True не нужен т.к. в БД это обычное текстовое поле.
    # max_length=1000 - по умолчанию значение 100, пару раз натыкался на глюки при длинных названиях файлов,
    # может в 1.5 уже и не нужно, но там все так же 100.
    avatar = models.ImageField(_(u'avatar'), upload_to='accounts/avatar/%Y/%m/', blank=True, max_length=1000)
    # Добавляем поле дня рождения.
    birthday = models.DateField(_(u'birthday'), blank=True, null=True)
    phone = models.CharField("Телефон", max_length=200, unique=True, blank=True)


class Address(models.Model):
    region = models.CharField("Область", max_length=200, blank=True)
    city = models.CharField("Город", max_length=200, blank=True)
    index = models.CharField("Индекс", max_length=200, blank=True)
    address = models.CharField("Адрес", max_length=200, blank=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", blank=True, null=True)