from django.db import models

# Create your models here.
class patient_generalinfo(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age=models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20) 
    email = models.EmailField()
    address = models.CharField(max_length=200)

class patient_healthinfo(models.Model):
    patient = models.OneToOneField(patient_generalinfo, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=20)
    height = models.IntegerField()
    weight = models.IntegerField()
    blood_pressure = models.CharField(max_length=30)
    symptoms = models.TextField()
    disease = models.CharField(max_length=200)
    treatment = models.TextField()
    diagnosis_date = models.DateField()
    doctor_name = models.CharField(max_length=100)

