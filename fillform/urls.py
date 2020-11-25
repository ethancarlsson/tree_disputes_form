from django.urls import path
from . import views

app_name = 'fillform'
urlpatterns = [
    path('', views.index, name='index'),
]