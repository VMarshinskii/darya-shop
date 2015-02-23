from django.contrib import admin
from shop.models import UserCart, TypeDelivery, Order

# Register your models here.
admin.site.register(UserCart)
admin.site.register(TypeDelivery)
admin.site.register(Order)