from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.forms import *

   



def create_student(request):
    ESFO=Studentform()
    d={'ESFO':ESFO}

    if request.method=='POST':
       SFDO=Studentform(request.POST)
       if SFDO.is_valid():
          SFDO.save()
          return HttpResponse('Successfully insert')
       else:
          return HttpResponse('Invalid')


    return render(request,'create_student.html',d)