from django.contrib import admin
from shop.models import UserCart, TypeDelivery, Order


class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'status', 'admin_comment')


admin.site.register(UserCart)
admin.site.register(TypeDelivery)
admin.site.register(Order, AdminOrder)