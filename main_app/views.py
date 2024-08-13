from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# Define the home view function
def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

# main_app/views.py
def about(request):
    return render(request, 'about.html')
