# -*- coding: utf-8 -*-
from django.forms import ModelForm
from models import Order
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['type_delivery', 'name', 'surname', 'mail', 'phone', 'region', 'city', 'index', 'address']


class OrderForm2(forms.Form):
    address_id = forms.CharField(max_length=200)
    type_delivery = forms.CharField(max_length=200)
    region = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    index = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200, widget=forms.Textarea)


class OrderForm3(forms.Form):
    address_id = forms.CharField(max_length=200)
    type_delivery = forms.CharField(max_length=200)