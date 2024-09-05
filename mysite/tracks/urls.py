
from django.urls import path

from tracks.views import  landing, index, create, show


urlpatterns=[
    path('land', landing, name='landing'),
    path('index', index, name='tracks.index'),
    path('create', create, name='tracks.create'),
    path("<int:id>", show, name='tracks.show')
]