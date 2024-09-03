
from django.urls import path
from students.views import (hello, landing, get_students, student_details,
                            land_with_temp,  index, show)

urlpatterns = [
    # path(url , viewfunc, url_name)
    path('hello', hello, name='hello'),
    path('land', landing, name='landing'),
    path('stds', get_students, name='stds'),
    path('stds/<int:id>', student_details, name='student_details'),
    path('template', land_with_temp, name='land_with_temp'),
    path('index', index, name='students.index'),
    path('<int:id>', show, name='students.show'),

]
