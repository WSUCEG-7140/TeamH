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
