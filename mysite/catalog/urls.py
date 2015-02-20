from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'catalog.views.home'),
    url(r'^product/(?P<id>\d+)/$', 'catalog.views.product'),
    url(r'^(?P<url>[\-\w]+)/$', 'catalog.views.category')
)
