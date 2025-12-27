from django.contrib import admin
from .models import Wallet, Payment

# Register your models here.

admin.site.register(Wallet)
admin.site.register(Payment)