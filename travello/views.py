from django.shortcuts import render
from .models import Destination
# Create your views here.
from django.http import HttpResponse

def index(request):

    dests = Destination.objects.all()
    return render(request, 'index.html',{'dests': dests})

def contact(request):

    return render(request,'contact.html')

def destinations(request):

    return render(request,'destinations.html')

def destinations1(request):
    dests = Destination.objects.all()
    return render(request,'destinations1.html',{'dests':dests})

def register1(request):

    if  request.method == 'POST':
        # name=request.POST['name']
        # add=request.POST['add']
        # email=request.POST['email']
        # phone=request.POST['phone']    

        # user = User.objects.create_user(name=name,add=add,email=email,phone=phone)
        registration.name= request.POST.get('name')
        registration.save();
        return redirect('')
    else:

        return render(request,'desti.html')