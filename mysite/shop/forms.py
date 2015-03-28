# -*- coding: utf-8 -*-
from django import forms
from models import Order
from redactor.widgets import RedactorEditor


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['type_delivery', 'name', 'surname', 'mail', 'phone', 'region', 'city', 'index', 'address']
        widgets = {
            'address': forms.Textarea(),
        }


class MailSenderForm(forms.Form):
    theme = forms.CharField(label='Тема письма', max_length=200)
    text = forms.CharField(widget=RedactorEditor())