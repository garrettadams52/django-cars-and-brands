from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand,Car

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def brands(request):
    return HttpResponse(Brand.objects.all())

def add_brand(request):
    pass
