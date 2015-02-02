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
            model.sale = int(request.POST['sale'])
            if 'sale_status' in request.POST:
                model.sale_status = request.POST['sale_status']
            else: model.sale_status = ''
            model.count = int(request.POST['count'])
            model.status = int(request.POST['status'])
            model.text = request.POST['text']
            model.keywords = request.POST['keywords']
            model.description = request.POST['description']
            model.save()
        csrf_token = get_token(request)
        return render_to_response('admin/product_form.html', {'csrf_token': csrf_token, 'model': model}, context_instance=RequestContext(request))


import_uploader = AjaxFileUploader()