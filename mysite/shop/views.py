# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404


# Create your views here.
def cart(request):
    return render_to_response("cart.html")