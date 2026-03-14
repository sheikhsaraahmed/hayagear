from django.shortcuts import render
from .models import Designer

def home(request):
    designers = Designer.objects.all()
    return render(request, "home.html", {"designers": designers})