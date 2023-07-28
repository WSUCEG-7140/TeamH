# Design

This design document outlines the architecture and key components of the system, providing an overview of its functionalities and interactions following the Model-View-Controller (MVC) design pattern with @ref Requirements.

@section Project Project Overview

The Patient Record Management System is a web application developed using Django, designed to help healthcare professionals efficiently manage patient records.

# Features
1.	Patient Record Creation: Healthcare professionals can add new patient records to the system.
2.	Patient Record Listing: The system provides a list of all patients with their basic information (e.g., name, age, gender) for quick reference.
3.	Search Functionality: Users can search for specific patients based on their email addresses or other criteria.
4.	Detailed Patient View: The system offers a detailed view of individual patient records, displaying all relevant information.
5.  Editing and Updating Records: Changes to patient records are securely saved to the database.
6.  Deletion of Patient Records: Patient Records can be deleted when necessary.

@section ModelViewController Model View Controller

This design applies the [Model View Controller](https://en.wikipedia.org/wiki/Model–view–controller) Design Pattern.

## Model

The Model consists of the following component:

@anchor R3_0 https://github.com/WSUCEG-7140/TeamH/blob/main/PatientInfoapp/models.py<br>

## View

The View consists of the following components:

@anchor R9_0 https://github.com/WSUCEG-7140/TeamH/blob/main/PatientInfoapp/templates/PatientInfoapp/home.html<br>
@anchor R15_0 https://github.com/WSUCEG-7140/TeamH/blob/main/PatientInfoapp/templates/PatientInfoapp/add_patient.html<br>
@anchor R17_0 https://github.com/WSUCEG-7140/TeamH/blob/main/PatientInfoapp/templates/PatientInfoapp/edit_patient.html<br>
@anchor R18_0 https://github.com/WSUCEG-7140/TeamH/blob/main/PatientInfoapp/templates/PatientInfoapp/patient_detail.html


## Controller

The Controller consists of the following component:

@anchor R4_0 https://github.com/WSUCEG-7140/TeamH/blob/main/PatientInfoapp/views.py

## Forms

Defines Django forms for data validation and handling user input, such as adding and editing patient records.

@anchor R30_0 https://github.com/WSUCEG-7140/TeamH/blob/main/PatientInfoapp/forms.py

## URLs

Maps URLs to corresponding views (controllers) in views.py, allowing users to access different pages and functionalities of the application. 
