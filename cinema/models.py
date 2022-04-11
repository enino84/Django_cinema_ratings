from django.db import models
import datetime

# Create your models here.


class Owner(models.Model):
    username = models.EmailField(primary_key=True);
    password = models.CharField(max_length=30);
    fullname = models.CharField(max_length=30);


class Movie(models.Model):
    owner    = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name     = models.CharField(max_length=30);
    stars    = models.IntegerField();
    release  = models.DateTimeField(blank=True, null=True, default=datetime.date.today)
    classpg  = models.CharField(max_length=5);
    comments = models.TextField(null=True);
    publicp  = models.BooleanField(default=True);
