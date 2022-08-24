from django.db import models

class Family_Members(models.Model) :
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    birthday = models.DateField()
    phone_number = models.IntegerField()
