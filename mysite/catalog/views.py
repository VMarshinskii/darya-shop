# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from django.middleware.csrf import get_token
from django.template import RequestContext
from catalog.models import Product
from ajaxuploader.views import AjaxFileUploader
from django.utils.encoding import smart_str


# Create your views here.
def home(request):
    return render_to_response("index.html")


def product(request):
    return render_to_response("product.html")


def product_form(request):
    model = Product()
    if request.method == 'POST':
        model.name = request.POST.get('name', '')
        model.price = int(request.POST.get('price', 0))
        model.sale = int(request.POST.get('sale', 0))
        model.sale_status = int(request.POST.get('sale_status', 0))
        model.count = int(request.POST.get('count', 0))
        model.count_status = int(request.POST.get('count_status', 0))
        model.status = int(request.POST.get('status', 0))
        model.text = request.POST.get('text', '')
        model.images = request.POST.get('images', '')
        model.related_products = request.POST.get('related_products', '')
        model.keywords = request.POST.get('keywords', '')
        model.description = request.POST.get('description', '')
        model.save()
    csrf_token = get_token(request)
    images = []
    return render_to_response('admin/product_form.html', {'csrf_token': csrf_token, 'model': model, 'img': images}, context_instance=RequestContext(request))


def product_edit(request, id=-1):
    if id != -1:
        model = Product.objects.get(id=id)
        if request.method == 'POST':
            model.name = request.POST.get('name', '')
            model.price = int(request.POST.get('price', 0))
            model.sale = int(request.POST.get('sale', 0))
            model.sale_status = int(request.POST.get('sale_status', 0))
            model.count = int(request.POST.get('count', 0))
            model.count_status = int(request.POST.get('count_status', 0))
            model.status = int(request.POST.get('status', 0))
            model.text = request.POST.get('text', '')
            model.images = request.POST.get('images', '')
            model.image = request.POST.get('image', '')
            model.related_products = request.POST.get('related_products', '')
            model.keywords = request.POST.get('keywords', '')
            model.description = request.POST.get('description', '')
            model.save()
        images = smart_str(model.images).split(';')
        for img in images:
            if img == '':
                images.remove(img)
        csrf_token = get_token(request)
        return render_to_response('admin/product_form.html', {'csrf_token': csrf_token, 'model': model, 'img': images}, context_instance=RequestContext(request))


def product_edit_afax_related(request):
    key = smart_str(request.GET.get('key'))
    models = Product.objects.filter(name__contains=key)[:7]
    return render_to_response('admin/edit_ajax_related.html', {'models': models})

import_uploader = AjaxFileUploader()