from django.contrib import admin
from .models import Item, Order, Transaction
# Register your models here.


admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Transaction)