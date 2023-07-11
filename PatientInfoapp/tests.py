from django.test import TestCase
from .models import patient_generalinfo, patient_healthinfo

# Create your tests here.
class PatientAppTestCase(TestCase):
    def setUp(self):
        self.general_info = {
            "first_name": "Sindhu",
            "last_name": "Kari",
            "age": 21,
            "gender": "Female",
            "phone_no": "178463934",
            "email": "kari.sindhu@gmail.com",
            "address": "Province,Cloveridge ct.",
        }
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
        



