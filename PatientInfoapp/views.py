from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import patient_generalinfo, patient_healthinfo
from .forms import GeneralInfoForm, HealthInfoForm
from django.db.models import Q

""" @ref R27_0"""
def patient_detail(request, pk):
    """
    @brief Display detailed information of a specific patient.
    @param request: The HTTP request object representing the user's request.
    @param pk: The primary key of the patient_generalinfo instance to be displayed.
    @return: A rendered HTML response displaying the detailed patient information.
    @pre: The database connection must be established and valid.
    @post: The patient_generalinfo instance corresponding to the provided primary key (pk) is retrieved
        from the database and rendered in the "patientInfoapp/patient_detail.html" template.
    """

    ##Get the patient_generalinfo instance based on the provided primary key(pk)
    patient = get_object_or_404(patient_generalinfo, pk=pk)

    ##Render "patientInfoapp/patient_detail.html" template, by passing patient as context
    return render(request, "PatientInfoapp/patient_detail.html", {"patient":patient})

""" @ref R6_0"""
def home(request):
    """
    @brief Display a list of patients with an optional search functionality.
    @param request: The HTTP request object representing the user's request.
    @return: A rendered HTML response displaying the list of patients or the search results if a search query is provided.
    @pre: The database connection must be established and valid.
    @post: The patient_generalinfo objects are retrieved from the database and rendered in the
        "PatientInfoapp/home.html" template. If a search query is provided, the list is filtered
        based on email addresses containing the search_email value.
    """

    # Retrieve the value of "search_email" parameter from the request's GET parameters
    search_email = request.GET.get("search_email")
    # Check if a search_email value is provided
    if search_email:
        # If search_email is provided, filter the patient_generalinfo objects based on email containing the search_email value
        patients = patient_generalinfo.objects.filter(email__icontains=search_email)
    else:
        # If search_email is not provided, fetch all patient_generalinfo objects
        patients = patient_generalinfo.objects.all()
    # Render the "home.html" template with the patients queryset as context data
    return render(request, "PatientInfoapp/home.html", {"patients": patients})

""" @ref R4_0"""
def add_patient(request):
    """
    @brief Display a form to add a new patient and process the form submission.
    @param request: The HTTP request object representing the user's request.
    @return: If the request method is POST and the submitted form data is valid, the view will create new
            patient_generalinfo and patient_healthinfo instances in the database and redirect the user to the "home" page.
            Otherwise, it will render the "PatientInfoapp/add_patient.html" template with the forms to display the form to the user.
    @pre: The database connection must be established and valid.
    @post: If the form data is valid and the request method is POST, a new patient_generalinfo instance and a related
        patient_healthinfo instance are created in the database with the submitted data. The user is redirected to the "home" page
        to display the updated list of patients.
    """
    if request.method == "POST":
         # Initialize GeneralInfoForm with POST data
        general_form = GeneralInfoForm(request.POST)
        # Initialize HealthInfoForm with POST data
        health_form = HealthInfoForm(request.POST)
        # Check if both forms are valid
        if general_form.is_valid() and health_form.is_valid():
            general_info = general_form.save()
            health_info = health_form.save(commit=False)
            health_info.patient = general_info
            health_info.save()
            return redirect("home")
        # Check else condition is met
    else:
        general_form = GeneralInfoForm()
        health_form = HealthInfoForm()
        # Render the "add_patient.html" template and also pass the form instances as context variables
    return render(
            request,
            "PatientInfoapp/add_patient.html",
            {"general_form": general_form, "health_form": health_form},
    )

""" @ref R5_0"""
def edit_patient(request, pk):
    """
    @brief Display a form to edit patient information and process the form submission.
    @param request: The HTTP request object representing the user's request.
    @param pk: The primary key of the patient_generalinfo object to be edited.
    @return: If the request method is POST and the submitted form data is valid, the view will update the
            patient_generalinfo and patient_healthinfo instances in the database and redirect the user to the "home" page.
            Otherwise, it will render the "PatientInfoapp/edit_patient.html" template with the forms containing the
            existing patient information to display the form to the user.
    @pre: The database connection must be established and valid.
    @post: If the form data is valid and the request method is POST, the patient_generalinfo instance and its related
        patient_healthinfo instance are updated in the database with the edited data. The user is redirected to the "home" page
        to display the updated list of patients.
    """

    # Retrieve the patient_generalinfo object with the given pk (primary key)
    patient = patient_generalinfo.objects.get(pk=pk)
    
    # Retrieve the patient_healthinfo related to the patient
    health_info = patient.patient_healthinfo
    if request.method == "POST":
        # If the request method is POST, process the form data
        # Create instances of GeneralInfoForm and HealthInfoForm with the POST data and patient instances
        general_form = GeneralInfoForm(request.POST, instance=patient)
        health_form = HealthInfoForm(request.POST, instance=health_info)
        
        # Check if both general_form and health_form are valid
        if general_form.is_valid() and health_form.is_valid():
            # Save the updated data from the forms
            general_form.save()
            health_form.save()
            
            # Redirect the user to the "home" view
            return redirect("home")
    else:
        # If the request method is not POST, display the forms with the existing data
        # Create instances of GeneralInfoForm and HealthInfoForm with the patient instances
        general_form = GeneralInfoForm(instance=patient)
        health_form = HealthInfoForm(instance=health_info)    
    
    # Render the "edit_patient.html" template with the forms and patient as context data
    return render(
        request,
        "PatientInfoapp/edit_patient.html",
        {"general_form": general_form, "health_form": health_form, "patient": patient},
    )
""" @ref R7_0"""
def delete_patient(request, pk):
    """
    @brief Delete a patient from the database.
    @param request: The HTTP request object representing the user's request.
    @param pk: The primary key of the patient_generalinfo object to be deleted.
    @return: Upon successful deletion, the view redirects the user to the "home" view to display the updated list of patients.
    @pre: The database connection must be established and valid.
    @post: The patient_generalinfo instance corresponding to the provided primary key (pk) is deleted from the database.
    """

    # Retrieve the patient_generalinfo object with the given pk (primary key)
    patient = patient_generalinfo.objects.get(pk=pk)
    
    # Delete the patient object from the database
    patient.delete()
    
    # Redirect the user to the "home" view
    return redirect("home")