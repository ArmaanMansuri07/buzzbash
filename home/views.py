from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def clubs(request):
    return render(request, 'clubs.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')



def delhi(request):
    return render(request, 'delhi.html')

def noida(request):
    return render(request, 'noida.html')

def gurugram(request):
    return render(request, 'gurugram.html')