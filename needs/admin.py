from django.contrib import admin
from .models import Need
from .models import Question, ContactUs, Review

# Register your models here.

admin.site.register(Need)
admin.site.register(Question)
admin.site.register(ContactUs)
admin.site.register(Review)