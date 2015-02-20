from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'shop.views.cart'),
    url(r'^order/$', 'shop.views.order'),
    url(r'^add_in_cart/(?P<id>\d+)/$', 'shop.views.add_in_cart'),
    url(r'^del_in_cart/(?P<id>\d+)/$', 'shop.views.del_in_cart'),
    url(r'^remove_in_cart/(?P<id>\d+)/$', 'shop.views.remove_in_cart'),
    url(r'^cart_top_ajax/$', 'shop.views.cart_top_ajax')
)
