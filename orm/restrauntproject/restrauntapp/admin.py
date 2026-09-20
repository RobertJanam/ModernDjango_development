from django.contrib import admin
from .models import Restaurant, Chef, Cook, Waiter, Customer

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Chef)
admin.site.register(Cook)
admin.site.register(Waiter)
admin.site.register(Customer)