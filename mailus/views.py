from django.shortcuts import render

def home(request):
    return render(request, 'mailus/mailus.html', {'title':'Mail US'})
