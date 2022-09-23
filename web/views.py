from http.client import HTTPResponse
from django.shortcuts import render, redirect
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
def family(request, child):
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('addoption', family=form.instance.id, child=child)
        else:
            print(form.errors)
            return render(request, 'addoption.html', {'form': form},status=400)
    else:
        form = FamilyForm()
    return render(request, 'addoption.html', {'form': form})

def addoption(request, family, child):
    print("here")
    print(child)
    # add family to the POST request
    request.POST.family = family
    request.POST.child = child
    if request.method == 'POST':
        form = AddoptionForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.family = Family.objects.get(id=family)
            obj.child = Child.objects.get(id=child)
            obj.save()
            return render(request, 'success.html')
        else:
            print(form.errors)
            return render(request, 'addoption.html', {'form': form},status=400)
    else:
        form = AddoptionForm()
    return render(request, 'addoption.html', {'form': form})