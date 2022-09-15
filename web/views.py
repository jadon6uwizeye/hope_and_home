from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import Child
from .forms import AddoptionForm, FamilyForm
from .serializers import FamilySerializer
from dashboard.models import Family

# Create your views here.

def home(request):
    children = Child.objects.filter(family=None)
    return render(request, 'index.html', {"children": children})

@csrf_exempt
def family(request):
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'addoption.html', {"form": form}, status=201)
        else:
            print(form.errors)
            return render(request, 'addoption.html', {'form': form},status=400)
    else:
        form = FamilyForm()
    return render(request, 'addoption.html', {'form': form})

def addoption(request):
    if request.method == 'POST':
        form = AddoptionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'addoption.html', {"form": form}, status=201)
        else:
            print(form.errors)
            return render(request, 'addoption.html', {'form': form},status=400)
    else:
        form = AddoptionForm()
    return render(request, 'addoption.html', {'form': form})