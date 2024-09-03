from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def view function --> handle http request
def hello(request):
    print(request)
    return HttpResponse("Hello world from iti")



def landing(request):
    # request ---> represent http request ?
    return HttpResponse("<h1 style='text-align:center; color:red'>Hello world from iti</h1>")


def get_students(request):
    students = [
        {"id":1, "name":"hassan", "track": "python", "grade":100, "image":"pic1.png"},
        {"id": 2, "name": "Mohamed", "track": "python", "grade": 100, "image": "pic2.png"},
        {"id": 3, "name": "Mostafa", "track": "python", "grade": 100, "image": "pic3.png"},
        {"id": 4, "name": "Abc", "track": "python", "grade": 100, "image": "pic4.png"},
        {"id":5, "name":"test", "track": "python", "grade":100, "image":"pic5.png"},
    ]

    return HttpResponse(students)

##### get one student ??
def student_details(request, id):
    print(id, type(id))
    students = [
        {"id": 1, "name": "hassan", "track": "python", "grade": 100, "image": "pic1.png"},
        {"id": 2, "name": "Mohamed", "track": "python", "grade": 100, "image": "pic2.png"},
        {"id": 3, "name": "Mostafa", "track": "python", "grade": 100, "image": "pic3.png"},
        {"id": 4, "name": "Abc", "track": "python", "grade": 100, "image": "pic4.png"},
        {"id": 5, "name": "test", "track": "python", "grade": 100, "image": "pic5.png"},
    ]

    for student in students:
        if student["id"] == id:
            return HttpResponse(student.values())

    else:
        return HttpResponse("<h1 style='color:red'>Not found</h1>")


