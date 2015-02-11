from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^page/(?P<url>w+/$)', 'pages.views.page_view'),
)
