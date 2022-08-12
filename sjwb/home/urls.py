from django.urls import path
from home import datahandler, views

urlpatterns = [
	path('datahandler', datahandler.getdata),
    path('', views.TaiwanChart, name='TaiwanChart'),
]