# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea, TextInput, RegexField
from models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['type_delivery', 'name', 'surname', 'mail', 'phone', 'region', 'city', 'index', 'address']
        widgets = {
            'address': Textarea(),
            'phone': TextInput(attrs={'placeholder': '+7XXXXXXXXXX'}),

        }