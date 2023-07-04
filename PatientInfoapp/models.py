from django.db import models

# Create your models here.
class PatientGeneralInfo(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contactNumber = models.CharField(max_length=20)
    emailId = models.EmailField()
    address = models.CharField(max_length = 200)
    
    