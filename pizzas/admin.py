from django.contrib import admin
from .models import Toppings,Pizza,Order
# Register your models here.

admin.site.register(Toppings)
admin.site.register(Pizza)
admin.site.register(Order)