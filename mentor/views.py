from django.shortcuts import render
from .models import mentor_detail
from projects.models import project #need to import the model before using it

def home(request):

    #to get all the details of the mentor
    mentors = mentor_detail.objects.all()

    #if there is any search query
    query = request.GET.get("Search")

    if query:
        #Filtering the data according to the requested search
        mentors = mentors.filter(name__contains=query)

    context = {
            'mentors' : mentors
        }


    return render(request, 'mentor/mentor.html', context)

#For details of mentors
def sp_mentor(request , value):
	projects = project.objects.all()
	mentors = mentor_detail.objects.all()
	context = {'mentors':mentors,'name':value , 'projects' : projects}
	return render(request , 'mentor/sp_mentor.html' , context)