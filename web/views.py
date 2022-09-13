from django.shortcuts import render
from dashboard.models import Child

# Create your views here.

def home(request):
    children = Child.objects.filter(family=None)
    return render(request, 'index.html', {"children": children})