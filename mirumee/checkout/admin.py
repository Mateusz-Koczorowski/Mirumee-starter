from django.contrib import admin
from .models import Checkout, CheckoutLine, Order

# Register your models here.

admin.site.register(Checkout)
admin.site.register(CheckoutLine)
admin.site.register(Order)