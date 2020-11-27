from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from  django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import Sensor
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
username=''
password=''


def Index(request):
    global username, password
    user = authenticate(username=username, password=password)
    if user is not None:
        queryset = Sensor.objects.all()
        ar=[]
        for i in queryset:
            ar.append([i.longitude,i.latitude])
        return render(request,'index.html',{'object_list':ar})
    else:
        return HttpResponseRedirect(reverse('login'))

def LogIn(request):
    global username,password
    username=''
    password=''
    return HttpResponseRedirect(reverse('login'))
def LogIn(request):
    global username,password
    if request.method == 'POST': # If the form has been submitted...

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html', {'user': "Can not login. Try again",'error':True})
    else:
        return render(request,'login.html',{'error':False})


def Registar(request):
    global username, password
    if request.method == 'POST': # If the form has been submitted...
        name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        ps = request.POST.get("password_repeat")
        if(ps!=password):
            render(request, 'register.html', {'pass': "Password does not match", "pass_e":True,"user_e":False})
        try:

            user = User.objects.create_user(username=name,
                                        last_name=last_name,
                                        email=email,
                                        password=password)
            user.save()
            login(request, user)
        except:
            return render(request,'register.html', {'user': "Can not create a user","pass_e":False,"user_e":True})
        username=name
        password=password
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,'register.html')


