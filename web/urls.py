from django.urls import path
from django.conf.urls import url, include
from .views import Index, LogIn,Registar
urlpatterns = [

    path('', Index.as_view(), name='index'),
    path('login/', LogIn, name='login'),
    path('signup/', Registar, name='signup'),

]