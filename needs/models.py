from django.db import models
from users.models import UserProfile
# from .offers import Offers


# Create your models here.

class Needs(models.Model):
    name = models.CharField(max_length=100 , null=False , blank=False , unique=True)
    # id by default exists

    # Relation with users by user_id
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # Relation with offers by offer_id
    # offer_id = models.ForeignKey(Offers, on_delete=models.CASCADE)