from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Sensor
from .models import Registar as reg
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import datetime
from .models import Registar as ref,Sensor,Region
from django_pandas.io import read_frame
from django.core.mail import send_mail
import pandas as pd
username = ''
password = ''


def proc(request):
    global username, password
    user = authenticate(username=username, password=password)
    if user is not None:
        if 'proc1' in request.POST:
            qs = ref.objects.all()
            df = read_frame(qs)
            date1 = request.POST.get("pc1_d1")
            date2 = request.POST.get("pc1_d2")
            date1 = datetime.datetime.strptime(date1, '%Y-%m-%dT%H:%M')
            date2 = datetime.datetime.strptime(date2, '%Y-%m-%dT%H:%M')
            data = df[(df['date'] >= date1.date()) & (df['date'] <= date2.date()) & (df['time'] > date1.time()) & (df['time'] < date2.time())]
            data = data['temperature']
            send_mail(username, data.to_string(), 'maksimka.ivashkevich27@gmail.com', [user.email])
        if 'proc2' in request.POST:
            qs = ref.objects.all()
            df = read_frame(qs)
            time1 = request.POST.get("pc2_d1")
            time2 = request.POST.get("pc2_d2")
            time_object1 = datetime.datetime.strptime(time1, '%H:%M').time()
            time_object2 = datetime.datetime.strptime(time2, '%H:%M').time()
            data = df[(df['time'] > time_object1) & (df['time'] < time_object2)]
            str = f"Max tem in range {data['temperature'].max()}  and min {data['temperature'].min()}"
            send_mail(username, str, 'maksimka.ivashkevich27@gmail.com', [user.email])
        if 'proc3' in request.POST:
            qs = ref.objects.all()
            df = read_frame(qs)
            df['dev']=df.temperature- df.temperature.std()
            send_mail(username, df['dev'].to_string(), 'maksimka.ivashkevich27@gmail.com', [user.email])
        if 'proc4' in request.POST:
            qs = Sensor.objects.all()
            df = read_frame(qs)
            qs1 = Region.objects.all()
            df1 = read_frame(qs1)
            str_n = request.POST.get("str")
            df1 = df1[df1['nameregion']==str_n]
            df['regionid']= df['regionid'].str.replace('\\D','',regex=True).astype(int)
            buff = pd.merge(df1, df, left_on="regionid", right_on="regionid")
            buff = buff[['longitude','longitude']]
            buff = buff.to_string()
            send_mail(username, buff, 'maksimka.ivashkevich27@gmail.com', [user.email])
        return render(request, 'data.html', locals())
    else:
        return HttpResponseRedirect(reverse('login'))
class AboutView(TemplateView):
    template_name = "data.html"


def Table(request):
    global username, password
    user = authenticate(username=username, password=password)
    S = Sensor.objects.all()
    if user is not None:
        return render(request, 'table.html', locals())
    else:
        return HttpResponseRedirect(reverse('login'))


def data(request):
    date = []
    temp = []
    queryset1 = reg.objects.all()
    for i in queryset1:
        date.append(i.date)
        temp.append(i.temperature)
    return JsonResponse(data={
        'date': date,
        'temp': temp,
    })


def Index(request):
    global username, password
    user = authenticate(username=username, password=password)
    if user is not None:
        queryset = Sensor.objects.all()
        ar = []
        for i in queryset:
            ar.append([i.longitude, i.latitude])
        return render(request, 'index.html', {'object_list': ar})
    else:
        return HttpResponseRedirect(reverse('login'))


def LogIn(request):
    global username, password
    username = ''
    password = ''
    return HttpResponseRedirect(reverse('login'))


def LogIn(request):
    global username, password
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html', {'user': "Can not login. Try again", 'error': True})
    else:
        return render(request, 'login.html', {'error': False})


def Registar(request):
    global username, password
    if request.method == 'POST':  # If the form has been submitted...
        name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        ps = request.POST.get("password_repeat")
        if (ps != password):
            render(request, 'register.html', {'pass': "Password does not match", "pass_e": True, "user_e": False})
        try:

            user = User.objects.create_user(username=name,
                                            last_name=last_name,
                                            email=email,
                                            password=password)
            user.save()
            login(request, user)
        except:
            return render(request, 'register.html', {'user': "Can not create a user", "pass_e": False, "user_e": True})
        username = name
        password = password
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'register.html')
