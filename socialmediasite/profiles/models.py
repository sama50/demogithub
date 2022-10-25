from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    following = models.ManyToManyField(User,related_name="folwer")

