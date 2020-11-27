from django.urls import path
from django.conf.urls import url, include
from .views import Index, LogIn, Registar


urlpatterns = [

    path('', Index, name='index'),
    path('login/', LogIn, name='login'),
    path('logout/', LogIn, name='logout'),
    path('signup/', Registar, name='signup'),

]
