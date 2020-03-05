from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.login, name='login'),
     path('dashboard/', views.dashboard, name='dashboard'),
    url(r'^RunStep/$', views.Run_Step, name='Run_Step'),
]
