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
        url = reverse("patient_detail",args=[self.patient.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Expecting a successful response (status code 200)
         
        self.assertContains(response, self.general_info["first_name"])
        self.assertContains(response, self.general_info["last_name"])
        self.assertContains(response, self.general_info["age"])
        self.assertContains(response, self.general_info["gender"])
        self.assertContains(response, self.general_info["phone_number"])
        self.assertContains(response, self.general_info["email"])
        self.assertContains(response, self.general_info["address"])
        self.assertContains(response, self.health_info["blood_group"])
        self.assertContains(response, self.health_info["height"])
        self.assertContains(response, self.health_info["blood_pressure"])
        self.assertContains(response, self.health_info["symptoms"])
        self.assertContains(response, self.health_info["disease"])
        self.assertContains(response, self.health_info["treatment"])
        self.assertContains(response, self.health_info["diagnosis_date"])
        self.assertContains(response, self.health_info["doctor_name"])

    
    """
    Test case to verify the view for displaying patient details.

    This test checks whether the patient details view is accessible, and if the
    patient's information is displayed correctly on the page.
    """    
    def test_view_patient_details(self):
        # Get the URL for viewing the details of a specific patient using the patient's primary key
        url = reverse("patient_detail", args=[self.patient.pk])
    
        # Send a GET request to retrieve the patient's details page
        response = self.client.get(url)
    
        # Verify that the page is accessible and the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verify that the patient's details are displayed correctly on the page  
        # Check if the response contains the patient's details
        self.assertContains(response, self.general_info["first_name"])
        self.assertContains(response, self.general_info["last_name"])
        self.assertContains(response, self.general_info["age"])
        self.assertContains(response, self.general_info["gender"])
        self.assertContains(response, self.general_info["phone_number"])
        self.assertContains(response, self.general_info["email"])
        self.assertContains(response, self.general_info["address"])
        self.assertContains(response, self.health_info["blood_group"])
        self.assertContains(response, self.health_info["height"])
        self.assertContains(response, self.health_info["blood_pressure"])
        self.assertContains(response, self.health_info["symptoms"])
        self.assertContains(response, self.health_info["disease"])
        self.assertContains(response, self.health_info["treatment"])
        self.assertContains(response, self.health_info["diagnosis_date"])
        self.assertContains(response, self.health_info["doctor_name"])

    """
    Test case to verify the deletion of a patient.
    This test checks whether a patient can be successfully deleted from the database
    when the corresponding view for deleting a patient is triggered. It also verifies
    that the patient is removed from the database and is no longer listed on the home page.
    """
    def test_delete_patient(self):
        # Get the URL for deleting the specific patient using the patient's primary key
        url = reverse("delete_patient", args=[self.patient.pk])
        # Send a POST request to trigger the deletion of the patient
        response = self.client.post(url)
    
        # Verify that the response status code is 302 (Redirect) after successful deletion
        self.assertEqual(response.status_code, 302)
        # Verify that the patient's records are deleted from both patient_generalinfo and patient_healthinfo tables
        self.assertEqual(patient_generalinfo.objects.count(), 0)
        self.assertEqual(patient_healthinfo.objects.count(), 0)

        # Verify that the deleted patient is no longer listed on the home page

        # Get the URL for the home page
        url = reverse("home")
        
        # Send a GET request to retrieve the home page
        response = self.client.get(url)
        
        # Verify that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the deleted patient details
        self.assertNotContains(response, self.general_info["first_name"])
        self.assertNotContains(response, self.general_info["last_name"])
        self.assertNotContains(response, self.general_info["age"])
        self.assertNotContains(response, self.general_info["gender"])
        self.assertNotContains(response, self.general_info["phone_number"])
        self.assertNotContains(response, self.general_info["email"])
        self.assertNotContains(response, self.general_info["address"])
        self.assertNotContains(response, self.health_info["blood_group"])
        self.assertNotContains(response, self.health_info["height"])
        self.assertNotContains(response, self.health_info["blood_pressure"])
        self.assertNotContains(response, self.health_info["symptoms"])
        self.assertNotContains(response, self.health_info["disease"])
        self.assertNotContains(response, self.health_info["treatment"])
        self.assertNotContains(response, self.health_info["diagnosis_date"])
        self.assertNotContains(response, self.health_info["doctor_name"])

    """
    Test case to verify searching patients by email on the home page.

    This test checks whether the search functionality for patients by email on the home
    page is working correctly. It verifies that only patients with matching email addresses
    are displayed on the home page when searching with a specific email.

    """
    def test_search_patients_by_email(self):
        # Get the URL for the home page
        url = reverse("home")
        
        # Send a GET request to the home page with a specific email in the data (search_email)
        response = self.client.get(url, data={"search_email": "kari.sindhu@gmail.com"})
        
        # Verify that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

         # Verify that only the patients with matching email addresses are displayed on the home page
        self.assertContains(response, self.general_info["first_name"])
        self.assertContains(response, self.general_info["last_name"])

        # Send another GET request to the home page with a different email in the data (search_email)
        response = self.client.get(url, data={"search_email": "jane.smith@example.com"})
        
        # Verify that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verify that the response does not contain the first name and last name of patients whose
        # email does not match the search criteria
        self.assertNotContains(response, self.general_info["first_name"])
        self.assertNotContains(response, self.general_info["last_name"])

    """
    Test case to verify editing patient information.

    This test checks whether the process of editing a patient's information is functioning correctly.
    It verifies that the edit page is accessible, the form submission results in a successful redirect,
    and the patient's details are updated correctly in the database. Additionally, it ensures that the
    updated patient's information is reflected on the home page.
    """
    def test_edit_patient(self):
        # Get the URL for editing the specific patient using the patient's primary key
        url = reverse("edit_patient", args=[self.patient.pk])
        
        # Send a GET request to retrieve the edit page
        response = self.client.get(url)
        
        # Verify that the page is accessible and the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Prepare modified general information and health information for the patient
        modified_general_info = {
        "first_name": "Jane",
        "last_name": "Smith",
        "age": 35,
        "gender": "Female",
        "phone_number": "9876543210",
        "email": "jane.smith@example.com",
        "address": "456 Elm St",
        }
        modified_health_info = {
        "blood_group": "B+",
        "height": 170,
        "weight": 65,
        "blood_pressure": "130/85",
        "symptoms": "Cough, sore throat",
        "disease": "Flu",
        "treatment": "Medication",
        "diagnosis_date": "2023-07-11",
        "doctor_name": "Dr. Johnson",
        }

        # Send a POST request with the modified information to update the patient's record
        response = self.client.post(
            url,
            data={
                **modified_general_info,
                **modified_health_info,
            },
        )
        
        # Verify that the response status code is 302 (Redirect) after successful submission
        self.assertEqual(response.status_code, 302)

        # Verify that the patient's general information is updated correctly in the database
        updated_patient = patient_generalinfo.objects.get(pk=self.patient.pk)
        self.assertEqual(updated_patient.first_name, modified_general_info["first_name"])
        self.assertEqual(updated_patient.last_name, modified_general_info["last_name"])
        self.assertEqual(updated_patient.age, modified_general_info["age"])
        self.assertEqual(updated_patient.gender, modified_general_info["gender"])
        self.assertEqual(updated_patient.phone_number, modified_general_info["phone_number"])
        self.assertEqual(updated_patient.email, modified_general_info["email"])
        self.assertEqual(updated_patient.address, modified_general_info["address"])
        
        # Verify that the patient's health information is updated correctly in the database
        updated_health_info = patient_healthinfo.objects.get(patient=self.patient)
        self.assertEqual(updated_health_info.blood_group, modified_health_info["blood_group"])
        self.assertEqual(updated_health_info.height, modified_health_info["height"])
        self.assertEqual(updated_health_info.weight, modified_health_info["weight"])
        self.assertEqual(updated_health_info.blood_pressure, modified_health_info["blood_pressure"])
        self.assertEqual(updated_health_info.symptoms, modified_health_info["symptoms"])
        self.assertEqual(updated_health_info.disease, modified_health_info["disease"])
        self.assertEqual(updated_health_info.treatment, modified_health_info["treatment"])
        self.assertEqual(
            updated_health_info.diagnosis_date.strftime("%Y-%m-%d"),
            modified_health_info["diagnosis_date"],
        )
        self.assertEqual(updated_health_info.doctor_name, modified_health_info["doctor_name"])
        # Verify that the updated patient is listed on the home page
        # Get the URL for the home page
        url = reverse("home")
        
        # Send a GET request to retrieve the home page
        response = self.client.get(url)
        
        # Verify that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)


        



       





  
