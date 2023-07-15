from django.contrib import admin

# Register your models here.
from .models import Category,Product,Market,Images,Comment,Sub_Category,Order_one,Order,Size,Address

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Market)
admin.site.register(Images)
admin.site.register(Comment)
admin.site.register(Sub_Category)
admin.site.register(Order_one)
admin.site.register(Order)
admin.site.register(Size)
admin.site.register(Address)
