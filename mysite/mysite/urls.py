from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'catalog.views.home'),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'ajax-upload$', 'catalog.views.import_uploader', name="my_ajax_upload"),
    url(r'^redactor/', include('redactor.urls')),
    url(r'/admin/catalog/product/add/$', 'catalog.views.product_form', name="start"),
)
