from http.client import HTTPResponse
from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
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

# send email to email from email given
def sendMail(request):
    if request.method == 'POST':
        try:
            print(request)
            name = request.POST.get('name')
            email = request.POST['email']
            message = request.POST['message']
            print(send_mail(
                'Hope and Home user email',
                f"Email from {name}, with email {email} has sent the following message \n\n {message}",
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            ))
            print("email sent \n\n", email)

            # redirect to home url
            return redirect('home')
        except Exception as e:
            print("error sending email\n\n\n\n\n")
            print(e)
            return redirect('home')

    else:
        return redirect('home')