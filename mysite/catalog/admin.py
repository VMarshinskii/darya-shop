from django.contrib import admin
from catalog.models import Product
from django.shortcuts import render_to_response


# Register your models here.
class ProductAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        vars = {'categories': "dsjfskdf"}
        html = render_to_response('admin/result_content_list.html', vars).content
        mass = {'result_content': html}
        return super(ProductAdmin, self).changelist_view(request, extra_context=mass)

    
admin.site.register(Product, ProductAdmin)