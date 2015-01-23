from django.shortcuts import render_to_response
from django.http import Http404


# Create your views here.
def home(request):
    return render_to_response("index.html")


def product(request):
    return render_to_response("product.html")