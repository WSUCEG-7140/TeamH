from django import forms
from .models import patient_generalinfo, patient_healthinfo

""" @ref R30_0"""
class GeneralInfoForm(forms.ModelForm):

    """
    @brief Form for capturing general patient information.

    @param forms.ModelForm: Base class for Model-based forms in Django.

    @pre `patient_generalinfo` model must be defined.

    @post An instance of this form can create or update a patient's general information.

    Attributes:
        model (patient_generalinfo): The Django model associated with this form.
        fields (list): The list of fields from the model to be included in the form.
    """
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

""" @ref R30_0"""
class HealthInfoForm(forms.ModelForm):

    """
    @brief Form for capturing patient health information.

    @param forms.ModelForm: Base class for Model-based forms in Django.

    @pre `patient_healthinfo` model must be defined.

    @post An instance of this form can create or update a patient's health information.

    Attributes:
        model (patient_healthinfo): The Django model associated with this form.
        fields (list): The list of fields from the model to be included in the form.
    """
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