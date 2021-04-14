from django.db import models
from phone_field import PhoneField

# Create your models here.
class Questions(models.Model):
    questions = models.CharField(max_length=500 , null=False , blank=False , unique=False)
    answer = models.CharField(max_length=500 , null=False , blank=False , unique=False)
    status = models.IntegerField()

    def __str__(self):
     return self.Questions


class ContactUs(models.Model):
    name = models.CharField(max_length=100 , null=False , blank=False , unique=False)
    email = models.EmailField(max_length = 254)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    message = models.CharField(max_length=1000 , null=False , blank=False , unique=False)
    seen = models.IntegerField()

    def __str__(self):
     return self.ContactUs


class Reviews(models.Model):
    content = models.CharField(max_length=100 , null=False , blank=False , unique=False)
    publish = models.IntegerField()

    def __str__(self):
     return self.Reviews