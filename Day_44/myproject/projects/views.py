from django.shortcuts import render, get_object_or_404
from .models import Projects



# Create your views here.

def projects_list(request):
    projects = Projects.objects.all()
    return render(request,'projects/projects_list.html',{'projects':projects})

def project_page(request, id):
    project = get_object_or_404(Projects ,id=id)
    return render(request, 'projects/project_page.html',{'project':project})
