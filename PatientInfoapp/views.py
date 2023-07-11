from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import patient_generalinfo, patient_healthinfo
from .forms import GeneralInfoForm, HealthInfoForm
from django.db.models import Q

def patient_detail(request, pk):
    #Get the patient_generalinfo instance based on the provided primary key(pk)
    patient = get_object_or_404(patient_generalinfo, pk=pk)

    #Render "patientInfoapp/patient_detail.html" template, by passing patient as context
    return render(request, "PatientInfoapp/patient_detail.html", {"patient":patient})

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
            "patientApp/add_patient.html",
            {"general_form": general_form, "health_form": health_form},
    )


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
        "patientApp/edit_patient.html",
        {"general_form": general_form, "health_form": health_form, "patient": patient},
    )