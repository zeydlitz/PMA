from django.urls import path
from django.conf.urls import url, include
from .views import Index, LogIn, Registar, Table,data

urlpatterns = [

    path('', Index, name='index'),
    path('login/', LogIn, name='login'),
    path('table/', Table, name='table'),
    path('logout/', LogIn, name='logout'),
    path('signup/', Registar, name='signup'),
    path('data/',data,name='data'),

]
