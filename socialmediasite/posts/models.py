from django.db import models
form profiles.models import person
# Create your models here.



class post(models.Model):
    name = models.CharField(max_length=30)