
from django.urls import path

from tracks.views import  landing, index


urlpatterns=[
    path('land', landing, name='landing'),
    path('index', index, name='tracks.index'),
]