# -*- coding: utf-8 -*-
from django.contrib import admin
from catalog.models import Product, Category
from django.shortcuts import render_to_response
from django.utils.encoding import smart_str


# Register your models here.
#class ProductAdmin(admin.ModelAdmin):

    #def changelist_view(self, request, extra_context=None):
    #    vars = {'categories': "dsjfskdf"}
    #    html = render_to_response('admin/result_content_list.html', vars).content
    #    mass = {'result_content': html}
    #    return super(ProductAdmin, self).changelist_view(request, extra_context=mass)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}

    def changelist_view(self, request, extra_context=None):
        list_category = sort_list()
        select_res(list_category)
        vars = {'categories': list_category}
        html = render_to_response('admin/result_content_list.html', vars).content
        mass = {'result_content': html}
        return super(CategoryAdmin, self).changelist_view(request, extra_context=mass)

    def save_model(self, request, obj, form, change):
        if obj.parent is None:
            obj.step = 0
        else:
            obj.step = obj.parent.step + 1
            obj.save()


def sort_list():
    mass_object = []
    roots = Category.objects.filter(parent=None)

    def rec_list(obj):
        obj.title = "sdfsadfjasdf"
        mass_object.append(obj)
        children = Category.objects.filter(parent=obj)

        for child in children:
            rec_list(child)

    for root in roots:
        rec_list(root)

    return mass_object


def select_res(categoryes):
    str_res = ""
    for category in categoryes:
        str_res += smart_str(category.title) + ":" + smart_str(category.id) + ";"
    return str_res

admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)