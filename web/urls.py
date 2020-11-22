from django.urls import path
from django.conf.urls import url, include
from .views import Index, LogIn,Registar
urlpatterns = [

    path('', Index.as_view(), name='index'),
    path('login/', LogIn.as_view(), name='login'),
    path('signup/', Registar.as_view(), name='signup'),

]