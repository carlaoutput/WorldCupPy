from django.contrib import auth
from django.db import models
from django.utils import timezone

# Blog models Created by CarlaPastor

class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)

#when a blog's user sign up django will take care of his info