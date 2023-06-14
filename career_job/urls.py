from django.urls import path
from . import views

urlpatterns = [
    path("search", views.search, name="search"),
    path(
        "job_applications/<slug:job_category_slug>/<slug:slug>",
        views.job_application,
        name="job_application",
    ),
    path(
        "job_creation_edit/<int:id>", views.job_creation_edit, name="job_creation_edit"
    ),
    path("job_creation", views.job_creation, name="job_creation"),
    path(
        "applicant_job_display",
        views.applicant_job_display,
        name="applicant_job_display",
    ),
    path("job_applied", views.job_applied, name="job_applied"),
    path("<slug:slug>", views.job_category_detail, name="job_category_detail"),
    path("<slug:job_category_slug>/<slug:slug>", views.job_detail, name="job_detail"),
    path("<slug:slug>", views.job_category_detail, name="job_category_detail"),
    path("<slug:job_category_slug>/<slug:slug>", views.job_detail, name="job_detail"),
]
