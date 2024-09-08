
from django.urls import path
from posts.views import  create
urlpatterns = [

    path('create',create, name='posts.create' )
]