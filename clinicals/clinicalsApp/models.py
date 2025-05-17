from django.db import models

# Create your models here.
class Patient(models.Model):
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    age = models.IntegerField()

class ClinicalData(models.Model):
    COMONENT_NAMES = [('hw', 'Height/Weight'), ('bp', 'Blood Pressure'), ('heartrate', 'Heart Rate')]
    componentName = models.CharField(choices=COMONENT_NAMES,max_length=100)
    componentValue = models.CharField(max_length=100)
    measuredDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)