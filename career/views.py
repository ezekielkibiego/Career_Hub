from django.shortcuts import render
from career_job.models import Job


# Create your views here.
def index(request):
    jobs = Job.objects.all()
    return render(request, "core/index.html", {"jobs": jobs})
