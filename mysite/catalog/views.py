from django.shortcuts import render_to_response
from django.http import Http404
from django.middleware.csrf import get_token
from django.template import RequestContext
from catalog.models import Product
from ajaxuploader.views import AjaxFileUploader


# Create your views here.
def home(request):
    return render_to_response("index.html")


def product(request):
    return render_to_response("product.html")


def product_form(request):
    if request.method == 'POST':
        model = Product()
        model.name = request.POST['name']
        model.price = int(request.POST['price'])
        model.sale = int(request.POST['sale'])
        model.sale_status = 1
        model.count = int(request.POST['count'])
        model.status = int(request.POST['status'])
        model.text = request.POST['text']
        model.keywords = request.POST['keywords']
        model.description = request.POST['description']
        model.save()
    csrf_token = get_token(request)
    return render_to_response('admin/product_form.html', {'csrf_token': csrf_token}, context_instance=RequestContext(request))

def product_edit(request, id=-1):
    if id != -1:
        model = Product.objects.get(id=id)
        if request.method == 'POST':
            model.name = request.POST['name']
            model.price = int(request.POST['price'])

            if 'sale' in request.POST:
                model.sale = int(request.POST['sale'])
            else: model.sale = 0

            model.sale_status = int(request.POST.get('sale_status', 0))

            if 'count_status' in request.POST:
                model.count_status = int(request.POST['count_status'])
            else: model.count_status = 0

            if 'count' in request.POST:
                model.count = int(request.POST['count'])
            else: model.count = 0

            if 'status' in request.POST:
                model.status = int(request.POST['status'])
            else: model.status = 0

            if 'text' in request.POST:
                model.text = request.POST['text']
            else: model.text = ''

            if 'images' in request.POST:
                model.images = request.POST['images']
            else: model.images = ''

            if 'related_products' in request.POST:
                model.related_products = request.POST['related_products']
            else: model.related_products = ''

            if 'keywords' in request.POST:
                model.keywords = request.POST['keywords']
            else: model.keywords = ''

            if 'description' in request.POST:
                model.description = request.POST['description']
            else: model.description = ''

            model.save()
        csrf_token = get_token(request)
        return render_to_response('admin/product_form.html', {'csrf_token': csrf_token, 'model': model}, context_instance=RequestContext(request))


import_uploader = AjaxFileUploader()