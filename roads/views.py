# import requests
from django.shortcuts import render

def road_page(request):
    return render(request, "roads/road.html")