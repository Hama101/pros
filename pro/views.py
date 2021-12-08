from django.shortcuts import render
from .models import *
# Create your views here.
def index(request , CIN):
    profile = Profile.objects.get(CIN=CIN)
    
    print("&&&&&&&&&&&&&&&&&&&& : ", profile.image.url)
    
    context = {
        "profile":  profile,
    }
    
    return render(request, 'index.html' , context)