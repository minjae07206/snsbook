from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "index.html")

def create(request):
    return render(request, 'create.html')

def search(request):
    return render(request, 'index.html')

def settings(request):
    return render(request, 'settings.html')