from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', 'shop.views.cart'),
    url(r'^order', 'shop.views.order'),
)
