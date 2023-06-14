from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login

# Create your views here.


def applicant_sign_up(request):
    form = Applicant_Creation_Form(request.POST)
    if request.method == "POST":
        form = Applicant_Creation_Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            applicant_type = user
            applicant_type.user_type = "applicant"
            applicant_type.save()
            login(request, user)

            return redirect("/")
    else:
        form = Applicant_Creation_Form()
    return render(request, "registration/applicant_sign_up.html", {"form": form})


# def applicant_profile(request):
#     if request.method == "POST":
#         form = ApplicantProfileForm(
#             request.POST,
#             request.FILES,
#             instance=ApplicantProfile.objects.get(user__id=request.user.id),
#         )
#         if form.is_valid():
#             form.save()

#             return redirect("applicant_profile")
#     else:
#         form = ApplicantProfileForm()

#     return render(request, "applicant_profile.html", {"form": form})


def overrall_register(request):
    return render(request, "registration/overrall_register.html")


def employer_sign_up(request):
    form = Employer_Creation_Form(request.POST)
    if request.method == "POST":
        form = Employer_Creation_Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            employer_type = user
            employer_type.user_type = "employer"
            employer_type.save()
            login(request, user)

            return redirect("/")
    else:
        form = Employer_Creation_Form()

    return render(request, "registration/employer_sign_up.html", {"form": form})


# def employer_profile(request):
#     if request.method == "POST":
#         form = EmployerProfileForm(
#             request.POST,
#             request.FILES,
#             instance=EmployerProfile.objects.get(user__id=request.user.id),
#         )
#         if form.is_valid():
#             form.save()

#             return redirect("employer_profile")
#     else:
#         form = EmployerProfileForm()

#     return render(request, "employer_profile.html", {"form": form})
def employer_profile_detail(request, pk):
    employer = Employer.employer.get(pk=pk)
    all = employer.jobs.all()
    return render(request, "profiles/employer_profile_detail.html", {"employer": employer, "job": all})
