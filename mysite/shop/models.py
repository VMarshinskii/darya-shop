# -*- coding: utf-8 -*-
from django.db import models


class UserCart(models.Models):
    user_key = models.CharField("Ключ", max_length=200)
    products = models.CharField("Товары", max_length=200)