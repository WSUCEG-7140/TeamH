from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import patient_generalinfo, patient_healthinfo
from .forms import GeneralInfoForm, HealthInfoForm
from django.db.models import Q

"""
    Display detailed information of a specific patient.

    This view retrieves the patient_generalinfo instance corresponding to the provided
    primary key (pk) from the database and renders the "patientInfoapp/patient_detail.html"
    template. The detailed patient information is passed to the template as the context.

    Parameters:
        request (HttpRequest): The HTTP request object representing the user's request.
        pk (int): The primary key of the patient_generalinfo instance to be displayed.

    Returns:
        HttpResponse: A rendered HTML response displaying the detailed patient information.
                      If the patient with the specified primary key does not exist in the
                      database, a 404 Not Found response will be returned.
"""
def patient_detail(request, pk):
    ##Get the patient_generalinfo instance based on the provided primary key(pk)
    patient = get_object_or_404(patient_generalinfo, pk=pk)

    ##Render "patientInfoapp/patient_detail.html" template, by passing patient as context
    return render(request, "PatientInfoapp/patient_detail.html", {"patient":patient})

"""
    Display a list of patients with an optional search functionality.

    This view retrieves a list of patient_generalinfo objects and allows users to search for
    specific patients based on their email addresses. If the "search_email" parameter is provided
    in the request's GET parameters, the view will filter the patient_generalinfo objects based on
    email addresses containing the search_email value. If "search_email" is not provided, the view
    will fetch all patient_generalinfo objects.

    Parameters:
        request (HttpRequest): The HTTP request object representing the user's request.

    Returns:
        HttpResponse: A rendered HTML response displaying the list of patients or the search
                      results if a search query is provided.
"""
def home(request):
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

"""
    Display a form to add a new patient and process the form submission.

    This view allows users to add a new patient to the system by presenting a form that collects
    both general information (e.g., name, age, gender) and health-related information (e.g., blood
    group, height, weight) of the patient. The view handles both displaying the form to the user
    and processing the form submission.

    Parameters:
        request (HttpRequest): The HTTP request object representing the user's request.

    Returns:
        HttpResponse: If the request method is POST and the submitted form data is valid,
                      the view will create new patient_generalinfo and patient_healthinfo
                      instances in the database and redirect the user to the "home" page.
                      Otherwise, it will render the "PatientInfoapp/add_patient.html" template
                      with the forms to display the form to the user.
"""
def add_patient(request):
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

"""
    Display a form to edit patient information and process the form submission.

    This view allows users to edit existing patient information by presenting a form that contains
    both the general information (e.g., name, age, gender) and health-related information (e.g.,
    blood group, height, weight) of the patient. The view handles both displaying the form with the
    existing data and processing the form submission when the user submits the edited information.

    Parameters:
        request (HttpRequest): The HTTP request object representing the user's request.
        pk (int): The primary key of the patient_generalinfo object to be edited.

    Returns:
        HttpResponse: If the request method is POST and the submitted form data is valid, the view
                      will update the patient_generalinfo and patient_healthinfo instances in the
                      database and redirect the user to the "home" page. Otherwise, it will render
                      the "PatientInfoapp/edit_patient.html" template with the forms containing the
                      existing patient information to display the form to the user.
"""
def edit_patient(request, pk):
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


"""
    Delete a patient from the database.

    This view allows users to delete an existing patient from the database. When the view is
    accessed, it retrieves the patient_generalinfo object with the given primary key (pk) from
    the database and then deletes it. After successful deletion, the user is redirected to the
    "home" view, displaying the updated list of patients.

    Parameters:
        request (HttpRequest): The HTTP request object representing the user's request.
        pk (int): The primary key of the patient_generalinfo object to be deleted.

    Returns:
        HttpResponseRedirect: Upon successful deletion, the view redirects the user to the
                                 "home" view to display the updated list of patients.
"""
def delete_patient(request, pk):
    # Retrieve the patient_generalinfo object with the given pk (primary key)
    patient = patient_generalinfo.objects.get(pk=pk)
    
    # Delete the patient object from the database
    patient.delete()
    
    # Redirect the user to the "home" view
    return redirect("home")