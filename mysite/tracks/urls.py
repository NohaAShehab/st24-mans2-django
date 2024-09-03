
from django.urls import path

from tracks.views import  landing


urlpatterns=[
    path('land', landing, name='landing'),

]