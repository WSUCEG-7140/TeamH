from django.test import TestCase
from django.urls import reverse
from .models import patient_generalinfo, patient_healthinfo

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

    def test_add_patient(self):
        # Get the URL for the "add_patient" view
        url = reverse("add_patient")
   
        # Test accessing the view with a GET request
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Expecting a successful response (status code 200)
    
        # Test submitting patient data via a POST request
        response = self.client.post(
            url,
            data={
                **self.general_info,  # Patient's general information (e.g., first name, last name, age)
                **self.health_info,   # Patient's health information (e.g., blood group, weight, blood pressure)
            },
    )
        # Expecting a redirect after successful submission (status code 302)
        self.assertEqual(response.status_code, 302)

        # Verify that the patient is added successfully to the database
        # Assuming there is already one patient in the database
        self.assertEqual(patient_generalinfo.objects.count(), 2)  # Check the count of general info objects
        self.assertEqual(patient_healthinfo.objects.count(), 2)   # Check the count of health info objects

        # Verify that the patient's information is listed on the home page
        url = reverse("patient_detail")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Expecting a successful response (status code 200)
    