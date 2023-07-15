from django.contrib import admin
from .models import Payment,Coupon,Credit_card
# Register your models here.

admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Credit_card)