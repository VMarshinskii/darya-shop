from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'catalog.views.home'),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^admin/catalog/product/add/$', 'catalog.views.product_form', name="start"),
    url(r'^admin/catalog/product/(?P<id>\d+)/$', 'catalog.views.product_edit', name="start"),
    url(r'^admin/catalog/product/edit_ajax_related/$', 'catalog.views.product_edit_afax_related'),
    url(r'^admin/catalog/product/edit_ajax_research/(?P<pr_id>\d+)$', 'catalog.views.product_edit_ajax_research'),
    url(r'^admin/email/', 'shop.views.admin_email'),
    url(r'^admin/settings/', 'accounts.views.admin_settings'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'ajax-upload$', 'catalog.views.import_uploader', name="my_ajax_upload"),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^cart/', include('shop.urls')),
    url(r'^login/', 'accounts.views.ajax_login'),
    url(r'^logout/', 'accounts.views.logout'),
    url(r'^registration/$', 'accounts.views.registration'),
    url(r'^user/orders/', 'accounts.views.my_orders'),
    url(r'^user/order/(?P<id>\d+)/$', 'accounts.views.my_order'),
    url(r'', include('pages.urls')),
)
