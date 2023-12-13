from django.contrib import admin
from register.models import register, verify_otp

# Register your models here.

admin.site.register(register)
admin.site.register(verify_otp)
