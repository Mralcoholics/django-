from django.shortcuts import render
from django.http import HttpResponse
from .form import medicallist
def home(request):
    form=medicallist()
    if request.method=='POST':
        form=medicallist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'sandy/home.html',context)
def AboutUs(request):
    form=medicallist()
    if request.method=='POST':
        form=medicallist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'sandy/About Us.html',context)
def AppointDoctor(request):
    form=medicallist()
    if request.method=='POST':
        form=medicallist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'sandy/Appoint Doctor.html',context)
def Login(request):
    form=medicallist()
    if request.method=='POST':
        form=medicallist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'sandy/Login.html',context)
def RegistraionForm(request):
    form=medicallist()
    if request.method=='POST':
        form=medicallist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'sandy/Registraion Form.html',context)
