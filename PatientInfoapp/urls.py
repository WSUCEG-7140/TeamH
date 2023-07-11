from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("patient/<int:pk>/", views.patient_detail, name="patient_detail"),
]
