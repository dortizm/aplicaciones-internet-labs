from django.shortcuts import render
from .models import Course, Student
from .services import generate_request

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html',{'valores':generate_request()})