# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from django.middleware.csrf import get_token
from django.template import RequestContext
from catalog.models import Product, Category
from ajaxuploader.views import AjaxFileUploader
from django.utils.encoding import smart_str
from catalog.admin import sort_list


# Create your views here.
def home(request):
    return render_to_response("index.html")


def product(request):
    return render_to_response("product.html")


def product_form(request):
    model = Product()
    model.price = 0
    model.sale = 0
    model.count = 0
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
        categories_id = int(request.POST.get('product_category', -1))
        model.home_status = 1
        if categories_id == -1:
            model.category = None
        else:
            model.category = Category.objects.get(id=categories_id)
        model.save()
    images = []
    related_products = []
    categories = sort_list()

    csrf_token = get_token(request)
    return render_to_response('admin/product_form.html',
          {
              'csrf_token': csrf_token,
              'model': model,
              'img': images,
              'related_products': related_products,
              'categories': categories,
          }
          , context_instance=RequestContext(request))


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
            categories_id = int(request.POST.get('product_category', -1))
            model.home_status = 1
            if categories_id == -1:
                model.category = None
            else:
                model.category = Category.objects.get(id=categories_id)
            model.save()
        images = smart_str(model.images).split(';')
        related_products = []
        categories = sort_list()

        for img in images:
            if img == '':
                images.remove(img)

        for pr in smart_str(model.related_products).split(';'):
            if pr != '':
                related_products.append(Product.objects.get(id=int(pr)))

        csrf_token = get_token(request)
        return render_to_response('admin/product_form.html',
              {
                  'csrf_token': csrf_token,
                  'model': model,
                  'img': images,
                  'related_products': related_products,
                  'categories': categories,
              }
              , context_instance=RequestContext(request))


def product_edit_afax_related(request):
    key = smart_str(request.GET.get('key'))
    models = Product.objects.filter(name__contains=key)[:7]
    return render_to_response('admin/edit_ajax_related.html', {'models': models, 'key': key})


def product_edit_ajax_research(request, pr_id=-1):
    if pr_id == -1:
        return Http404
    pr = Product.objects.get(id=pr_id)
    return render_to_response("admin/edit_ajax_research.html", {'product': pr})


import_uploader = AjaxFileUploader()