from django.shortcuts import render

# Create your views here.
def teacherhome(request):
    return render(request,"home_teacher.html")