from django.shortcuts import render_to_response
from django.http import Http404
from django.middleware.csrf import get_token
from django.template import RequestContext

from ajaxuploader.views import AjaxFileUploader


# Create your views here.
def home(request):
    return render_to_response("index.html")


def product(request):
    return render_to_response("product.html")


def start(request):
    csrf_token = get_token(request)
    return render_to_response('import.html', {'csrf_token': csrf_token}, context_instance=RequestContext(request))


import_uploader = AjaxFileUploader()