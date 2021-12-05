from django.contrib import admin
from .models import Payable, TypeOfService, Transaction, PaymentMethod

# Register your models here.
admin.site.register(Payable)
admin.site.register(TypeOfService)
admin.site.register(Transaction)
admin.site.register(PaymentMethod)