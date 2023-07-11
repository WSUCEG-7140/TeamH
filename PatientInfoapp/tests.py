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
        



