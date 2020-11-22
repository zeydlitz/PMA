from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from  django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

class Index(TemplateView):
    template_name = 'index.html'


def LogIn(request):
    if request.method == 'POST': # If the form has been submitted...

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'user': "Can not login. Try again",'error':True})
    else:
        return render(request,'login.html',{'error':False})


def Registar(request):
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
        return render(request, 'index.html')
    else:
        return render(request,'register.html')


