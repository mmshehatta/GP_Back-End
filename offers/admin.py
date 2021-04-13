from django.contrib import admin

# Register your models here.

from .models import Offer , Category

admin.site.register(Offer)
admin.site.register(Category)

