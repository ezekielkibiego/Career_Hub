from .models import *
from django import forms


class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "job_title",
            "job_description",
            "job_location",
            "position",
            "contract_type",
            "job_category",
        ]


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["job_title"]


class Cv_form(forms.ModelForm):
    class Meta:
        model = CV
        fields = ["cv_file"]
