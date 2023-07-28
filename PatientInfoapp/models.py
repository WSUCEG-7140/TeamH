from django.db import models

# Create your models here.
class patient_generalinfo(models.Model):
    
    """
    @brief Model for storing general information of a patient.

    @param models.Model: Base class for Django models.

    @pre None

    @post A new instance of patient_generalinfo is created in the database.

    Attributes:
        first_name (CharField): The first name of the patient (max length: 100 characters).
        last_name (CharField): The last name of the patient (max length: 100 characters).
        age (IntegerField): The age of the patient.
        gender (CharField): The gender of the patient (max length: 10 characters).
        phone_number (CharField): The phone number of the patient (max length: 20 characters).
        email (EmailField): The email address of the patient.
        address (CharField): The address of the patient (max length: 200 characters).
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age=models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20) 
    email = models.EmailField()
    address = models.CharField(max_length=200)

class patient_healthinfo(models.Model):

    """
    @brief Model for storing health-related information of a patient.

    @param models.Model: Base class for Django models.

    @pre patient_generalinfo model must be defined.

    @post A new instance of patient_healthinfo is created in the database and linked to a patient_generalinfo instance.

    Attributes:
        patient (OneToOneField): A one-to-one relationship with patient_generalinfo model.
        blood_group (CharField): The blood group of the patient (max length: 20 characters).
        height (IntegerField): The height of the patient in centimeters.
        weight (IntegerField): The weight of the patient in kilograms.
        blood_pressure (CharField): The blood pressure of the patient (max length: 30 characters).
        symptoms (TextField): The symptoms reported by the patient.
        disease (CharField): The disease diagnosed in the patient (max length: 200 characters).
        treatment (TextField): The treatment prescribed for the patient's condition.
        diagnosis_date (DateField): The date of diagnosis for the patient's condition.
        doctor_name (CharField): The name of the doctor who diagnosed and treated the patient (max length: 100 characters).
    """
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


