from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("patient/<int:pk>/", views.patient_detail, name="patient_detail"),
    path("add_patient/", views.add_patient, name="add_patient")
]
