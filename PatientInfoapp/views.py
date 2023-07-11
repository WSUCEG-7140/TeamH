from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import patient_generalinfo, patient_healthinfo
from django.db.models import Q

def patient_detail(request, pk):
    #Get the patient_generalinfo instance based on the provided primary key(pk)
    patient = get_object_or_404(patient_generalinfo, pk=pk)

    #Render "patientInfoapp/patient_detail.html" template, by passing patient as context
    return render(request, "patientApp/patient_detail.html", {"patient":patient})