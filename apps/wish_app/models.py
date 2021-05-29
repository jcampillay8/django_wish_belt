from django.db import models
import re
import bcrypt
from apps.login_register.models import User


class WishManager(models.Manager):
    def wish_validator(self, postData):
        errors = {}
        if len(postData['item']) < 3:
            errors['item'] = "Item must be no fewer than 3 characters."
        if len(postData['desc']) < 3:
            errors['first_name'] = "Description must be no fewer than 3 characters."
        return errors

class Wish(models.Model):
    item = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="wishes",on_delete=models.CASCADE)

    objects = WishManager()

class Granted_wish(models.Model):
    item = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now=True)
    granted_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')
    user = models.ForeignKey(User, related_name="granted_wishes", on_delete=models.CASCADE)