from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Account, Transaction  # ✅ import your models

# ✅ Register them so they appear in the admin site
admin.site.register(Account)
admin.site.register(Transaction)
