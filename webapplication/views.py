from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Django is MVC - this will contain what the user will see
# Django can communicate with other apps in websites - very transferable

def index(request):
    return HttpResponse("<h2>HEY</h2>")
