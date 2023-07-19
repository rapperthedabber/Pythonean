from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

def index(request):
    dest1 = Destination()
    dest1.name = 'JERRRYYY'
    dest1.description = 'Its actually Iron Man'

    dest2 = Destination()
    dest2.name= 'Tony Stark'
    dest2.description = 'I am not Ironman'

    dests = [dest1, dest2]
    return render(request,'index.html', {'dests': dests})
