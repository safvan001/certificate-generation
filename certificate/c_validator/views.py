from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from c_validator.models import Certificate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect

def home(request):
    return render(request,'base.html')

def create_certificate(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        subtitle = request.POST['subtitle']
        created_at=request.POST['created_at']
        signature=request.POST['signature']
        certificate = Certificate(user=user, name=name, subtitle=subtitle, created_at=created_at, signature=signature)
        certificate.save()
        messages.success(request, 'Certificate created successfully!')


    return render(request, 'create_certificate.html')

def verify_certificate(request):
    if request.method == 'POST':
        certificate_id = request.POST['certificate_id']
        return HttpResponse("Certificate is valid!")

    return render(request, 'verify_certificate.html')



# Create your views here.
