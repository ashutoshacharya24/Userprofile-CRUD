from django.db import models



class User(models.Model):
    name = models.CharField(max_length=50)
    userName = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50)
    phoneNumber = models.IntegerField(null=True, blank=False, unique=True)
    password = models.CharField(max_length=50)
    comment = models.CharField(default="", max_length=200)
    


