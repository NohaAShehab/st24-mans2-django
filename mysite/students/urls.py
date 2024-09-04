
from django.urls import path
from django.views.generic import edit

from students.views import (hello, landing, get_students, student_details,
        land_with_temp,  index, show, students_from_db, show_from_db, delete_from_db)

urlpatterns = [
    # path(url , viewfunc, url_name)
    path('hello', hello, name='hello'),
    path('land', landing, name='landing'),
    path('stds', get_students, name='stds'),
    path('stds/<int:id>', student_details, name='student_details'),
    path('template', land_with_temp, name='land_with_temp'),
    path('index', index, name='students.index'),
    path('<int:id>', show, name='students.show'),
    path('', students_from_db, name='students.db.index'),
    path('db/<int:id>', show_from_db, name='students.db.show'),
    path('delete/<int:id>', delete_from_db, name='students.db.delete'),
]
