from django.shortcuts import render
from .models import Designer, Product

def home(request):
    return render(request, 'index.html', {
        'designers': Designer.objects.all(),
        'products': Product.objects.all(),
    })