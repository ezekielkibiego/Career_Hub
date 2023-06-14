from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class Applicant_Creation_Form(UserCreationForm):
    class Meta:
        model = Applicant
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )


class ApplicantProfileForm(forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        fields = [
            "bio",
            "contact",
        ]


class Employer_Creation_Form(UserCreationForm):
    class Meta:
        model = Employer
        fields = (
            "email",
            "username",
            "full_name",
            "password1",
            "password2",
        )


class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ["bio", "contact", "hq"]
