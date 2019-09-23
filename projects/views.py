from django.shortcuts import render
from .models import project
from mentor.models import mentor_detail

def home(request):
    projects = project.objects.all()
    mentors = mentor_detail.objects.all()
    query = request.GET.get("Search")

    if query:

        projects = projects.filter(title__contains=query)

    context = {
            'projects' : projects, 'mentors' : mentors
        }


    return render(request, 'projects/projects.html', context)

def sp_project(request, value):
	projects = project.objects.all()
	context = {'projects' : projects, 'title' : value}
	return render(request , 'projects/sp_project.html' , context)