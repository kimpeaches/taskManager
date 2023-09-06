from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def project_list(request):
    list = Project.objects.filter(owner=request.user)
    context = {"project_list": list}
    return render(request, "projects/list.html", context)
