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
    products = Product.objects.filter(home_status=1)
    for pr in products:
        if pr.sale_status == 1:
                pr.new_price = (pr.price / 100) * (100 - pr.sale)
    return render_to_response("index.html", {'products': products})


def product(request, id=-1):
    if id != -1:
        product = Product.objects.get(id=id)
        images = []
        images_mass = product.images.split(";")
        for img in images_mass:
            if img != '' and img != product.image:
                images.append(img)
        related_products = []
        for pr in product.related_products.split(";"):
            if pr != '':
                try:
                    sop_pr = Product.objects.get(id=int(pr))
                    if sop_pr.sale_status == 1:
                        sop_pr.new_price = (sop_pr.price / 100) * (100 - sop_pr.sale)
                    related_products.append(sop_pr)

                except Product.DoesNotExist:
                    pass
        if product.sale_status == 1:
            product.new_price = (product.price / 100) * (100 - product.sale)
        return render_to_response("product.html", {
            'product': product,
            'images': images,
            'related_products': related_products
        })
    else:
        return Http404


def category(request, url="none"):
    try:
        categ = Category.objects.get(url=url)
        products = categ.get_all_product()
        for pr in products:
            if pr.sale_status == 1:
                pr.price_new = pr.price - (pr.price / 100 * pr.sale)
        path = list(reversed(categ.get_path_categ()))
    except Category.DoesNotExist:
        return Http404
    return render_to_response("category.html", {'path': path, 'categ': categ, 'products': products})


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
        model.home_status = int(request.POST.get('home_status', 0))
        categories_id = int(request.POST.get('product_category', -1))
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
            model.home_status = int(request.POST.get('home_status', 0))
            categories_id = int(request.POST.get('product_category', -1))
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