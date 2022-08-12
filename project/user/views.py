import re
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "login.html")

def teacherlogin(request):
    return render(request, "login teacher.html")
