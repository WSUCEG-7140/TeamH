from django.test import TestCase
from .models import patient_generalinfo, patient_healthinfo

#This class includes all the test methods
class PatientAppTestCase(TestCase):
    def setUp(self):
        #Adding test data for patient_generalinfo model 
        self.general_info = {
            "first_name": "Sindhu",
            "last_name": "Kari",
            "age": 21,
            "gender": "Female",
            "phone_no": "178463934",
            "email": "kari.sindhu@gmail.com",
            "address": "Province,Cloveridge ct.",
        }
        #Adding test data for patient_healthinfo model
        self.health_info = {
            "blood_group": "O+",
            "height": 175,
            "weight": 50,
            "blood_pressure": "120/80",
            "symptoms": "Fever, cold",
            "disease": "Common cold",
            "treatment": "take rest",
            "diagnosis_date": "2023-07-11",
            "doctor_name": "Dr. Srikanth",
        }
        #creating an instance for patient_generalinfo model by using above test data
        self.patient = patient_generalinfo.objects.create(**self.general_info)
        #linking the patient_generalinfo instance to patient_healthinfo  
        self.health_info["patient"] = self.patient
        #creating an instance for patient_healthinfo model by using above test data
        self.health = patient_healthinfo.objects.create(**self.health_info)
        



