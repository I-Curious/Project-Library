from django.shortcuts import render

#Simply used to render the about page with passing content title 
def home(request):
    return render(request, 'about/about.html', {'title':'Library Project'})
