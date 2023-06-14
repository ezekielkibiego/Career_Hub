from django.db import models
from career_auth.models import Employer, Applicant
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryImage
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your models here.


class Category(models.Model):
    title = models.CharField(
        max_length=200,
    )
    slug = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("Category", kwargs={"slug": self.slug})


class CV(models.Model):
    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name="applicant_cv"
    )

    cv_file = CloudinaryField("CV(PNG/JPEG)", null=True)
    date_applied = models.DateTimeField(auto_now=True, null=True)

    @property
    def cv_url(self):
        return (
            f"https://res.cloudinary.com/dlepgnfkx/{self.cv_file}"
        )

    def __str__(self):
        return self.cv_file


class Job(models.Model):
    positions = (
        ("junior", "junior"),
        ("intermediate", "intermediate"),
        ("senior", "senior"),
        ("expart", "expart"),
    )
    contaract_types = (
        ("remote", "remote"),
        ("part-time", "part-time"),
        ("full-time", "full-time"),
        ("negotiations", "negotiations"),
    )

    employer = models.ForeignKey(
        Employer, on_delete=models.CASCADE, related_name="jobs"
    )

    job_category = models.ForeignKey(
        Category,
        related_name="jobs",
        on_delete=models.CASCADE,
    )
    job_title = models.CharField(
        max_length=200,
    )
    slug = models.CharField(max_length=200, null=True)
    job_location = models.CharField(max_length=200)
    contract_type = models.CharField(max_length=200, choices=contaract_types)
    position = models.CharField(max_length=200, choices=positions)
    job_description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.job_title


class Job_Item(models.Model):
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name="all_jobs")
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,
                           related_name="all_jobs")

    def __str__(self):
        return self.job.job_title
