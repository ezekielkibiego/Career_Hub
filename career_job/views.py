from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

# Create your views here.


def job_detail(request, job_category_slug, slug):
    job_detail = get_object_or_404(Job, slug=slug)
    return render(request, "job/job_detail.html", {"job": job_detail})


def job_category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    job = category.jobs.all()
    return render(
        request, "job/job_category_detail.html", {
            "category": category, "job": job}
    )


def search(request):
    search = request.GET.get("search", "")
    jobs = Job.objects.filter(
        Q(job_title__icontains=search)
        | Q(job_description=search)
        | Q(job_location__icontains=search)
        | Q(contract_type=search)
        | Q(position__icontains=search)
    )

    return render(request, "job/search.html", {"search": search, "jobs": jobs})


@login_required(login_url="login")
def job_application(request, job_category_slug, slug):
    job_detail = get_object_or_404(Job, slug=slug)
    if request.method == "POST":
        form = Cv_form(
            request.POST,
            request.FILES,
            # instance=Job.objects.filter(applicant__id=request.user.id).first(),
        )
        if form.is_valid():
            user = form.save(commit=False)
            user.applicant = request.user
            user.save()
            Job_Item.objects.create(job=job_detail, cv=user).save()
            return redirect("/")
    else:
        form = Cv_form()

    return render(request, "job/job_application.html", {"form": form})


@login_required(login_url="login")
def applicant_job_display(request):
    job_item = Job_Item.objects.filter(cv__applicant=request.user)
    return render(request, "job/my_applications.html", {"job_item": job_item})


@login_required(login_url="login")
def job_creation(request):
    if request.method == "POST":
        title = request.POST.get("job_title")
        form = JobCreationForm(
            request.POST,
            request.FILES,
            # instance=Job.objects.filter(employer__id=request.user.id).first(),
        )
        if form.is_valid():
            user = form.save(commit=False)
            user.employer = request.user
            user.slug = slugify(title)
            user.save()
            return redirect("job_creation")

    else:
        form = JobCreationForm()

    return render(request, "job/job_creation.html", {"form": form})


@login_required(login_url="login")
def job_creation_edit(request, id):
    job = Job.objects.filter(employer=request.user).get(id=id)
    if request.method == "POST":
        form = JobCreationForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = JobCreationForm(instance=job)

    return render(request, "job/job_creation_edit.html", {"form": form})


@login_required(login_url="login")
def job_applied(request):
    job_item = Job_Item.objects.filter(job__employer=request.user)
    return render(request, "job/job_applied.html", {"job_item": job_item})
