
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100 , null=False , blank=False , unique=False)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length = 254)
    image = models.ImageField(upload_to='users/UserProfile/images' , null=True , blank=True)

    def __str__(self):
        return '%s' % self.user

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile, sender=User)
