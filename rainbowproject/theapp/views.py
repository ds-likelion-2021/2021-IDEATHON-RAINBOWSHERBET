from django.shortcuts import render

# Create your views here.
def road(requests):
    return render(requests, 'main.html')

def login(requests):
    return render(requests, 'login.html')