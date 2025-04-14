from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField(default=0.0)
    email = models.EmailField(max_length=50, unique=True)