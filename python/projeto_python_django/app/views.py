from django.shortcuts import render

def home(request):
    return render(request, 'app/index1.html')  # Página inicial

def index2(request):
    return render(request, 'app/index2.html')  # Página 2

def index3(request):
    return render(request, 'app/index3.html')  # Página 3
