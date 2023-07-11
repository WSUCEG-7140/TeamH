from django.test import TestCase
from .models import patient_generalinfo, patient_healthinfo
from django.urls import reverse

#This class includes all the test methods
class PatientAppTestCase(TestCase):
    def setUp(self):
        #Adding test data for patient_generalinfo model 
        self.general_info = {
            "first_name": "Sindhu",
            "last_name": "Kari",
            "age": 20,
            "gender": "Female",
            "phone_number": "178463934",
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

    #test case for patient_generalinfo attributes    
    def test_patient_generalinfo(self):
        self.assertEqual(self.patient.first_name, 'Sindhu')
        self.assertEqual(self.patient.last_name, 'Kari')
        self.assertEqual(self.patient.age, 20)
        self.assertEqual(self.patient.gender, 'Female')
        self.assertEqual(self.patient.phone_number, '178463934')
        self.assertEqual(self.patient.email, 'kari.sindhu@gmail.com')
        self.assertEqual(self.patient.address, 'Province,Cloveridge ct.')   

    #test case for patient_healthinfo attributes
    def test_patient_healthinfo(self):
        self.assertEqual(self.health.patient, self.patient)
        self.assertEqual(self.health.blood_group, 'O+')
        self.assertEqual(self.health.height, 175)
        self.assertEqual(self.health.weight, 50)
        self.assertEqual(self.health.blood_pressure, '120/80')
        self.assertEqual(self.health.symptoms, 'Fever, cold')
        self.assertEqual(self.health.disease, 'Common cold')
        self.assertEqual(self.health.treatment, 'take rest')
        self.assertEqual(str(self.health.diagnosis_date), '2023-07-11')
        self.assertEqual(self.health.doctor_name, 'Dr. Srikanth')  

    #unit test for a Django view that displays patient details
    def test_view_patient_details(self):
        # Create the URL for the patient detail view
        url = reverse("patient_detail", args=[self.patient.pk])
        # To the URL, send a GET request
        response = self.client.get(url)
        # Verify that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verify that the patient's details are displayed correctly
        self.assertContains(response, self.general_info["first_name"])
        self.assertContains(response, self.general_info["last_name"])
        self.assertContains(response, self.general_info["age"])
        self.assertContains(response, self.general_info["gender"])
        self.assertContains(response, self.general_info["phone_number"])
        self.assertContains(response, self.general_info["email"])
        self.assertContains(response, self.general_info["address"])
        self.assertContains(response, self.health_info["blood_group"])  
        self.assertContains(response, self.general_info["symptoms"])
        self.assertContains(response, self.general_info["disease"])
        self.assertContains(response, self.general_info["treatment"])
        self.assertContains(response, self.general_info["diagnosis_date"])
        self.assertContains(response, self.general_info["doctor_name"])

        



