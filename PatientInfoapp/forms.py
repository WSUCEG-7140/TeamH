from django import forms
from .models import patient_generalinfo, patient_healthinfo

class GeneralInfoForm(forms.ModelForm):
    class Meta:
        model = patient_generalinfo
        fields = [
            "first_name",
            "last_name",
            "age",
            "gender",
            "phone_number",
            "email",
            "address",
        ]

class HealthInfoForm(forms.ModelForm):
    class Meta:
        model = patient_healthinfo
        fields = [
            "blood_group",
            "height",
            "weight",
            "blood_pressure",
            "symptoms",
            "disease",
            "treatment",
            "diagnosis_date",
            "doctor_name",
        ]