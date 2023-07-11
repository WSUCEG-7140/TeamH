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
        