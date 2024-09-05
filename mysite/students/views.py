from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from students.models import Student
from students.forms import  StudentForm
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



### definew new view --> return with template

def land_with_temp(request):
    return render(request, "students/landing.html")
#
#
#
def index(request):
    students = [
        {"id": 1, "name": "hassan", "track": "python", "grade": 100, "image": "pic1.png"},
        {"id": 2, "name": "Mohamed", "track": "python", "grade": 100, "image": "pic2.png"},
        {"id": 3, "name": "Mostafa", "track": "python", "grade": 100, "image": "pic3.png"},
        {"id": 4, "name": "Abc", "track": "python", "grade": 100, "image": "pic4.png"},
        {"id": 5, "name": "test", "track": "python", "grade": 100, "image": "pic5.png"},
    ]
    return render(request, "students/index.html",
                  {"name":"noha", "students": students})


def show(request, id):
    students = [
        {"id": 1, "name": "hassan", "track": "python", "grade": 100, "image": "pic1.png"},
        {"id": 2, "name": "Mohamed", "track": "python", "grade": 100, "image": "pic2.png"},
        {"id": 3, "name": "Mostafa", "track": "python", "grade": 100, "image": "pic3.png"},
        {"id": 4, "name": "Abc", "track": "python", "grade": 100, "image": "pic4.png"},
        {"id": 5, "name": "test", "track": "python", "grade": 100, "image": "pic5.png"},
    ]


    for student in students:
        if student["id"] == id:
            return render(request, "students/show.html", {"student":student})

    return HttpResponse("<h1 style='color:red'>Not found</h1>")


############## using database



# view contact db --> via model to get data



def students_from_db(request):
    students = Student.objects.all()
    # students = Student.objects.filter(id__gt=2)
    return render(request, "students/db/index.html", {"students":students})



def show_from_db(request, id):
    # using filter
    # student= Student.objects.filter(id=id)  # queryset ??
    # return render(request, "students/db/show.html", {"student": student})

    # if student:
    #     student = student[0]
    #     return render(request, "students/db/show.html", {"student":student})
    # return HttpResponse("<h1 style='color:red'>Not found</h1>")

    # using get ??
    # student = Student.objects.get(id=id) # raise error
    # return render(request, "students/db/show.html", {"student":student})

    # using get_or_404
    student =get_object_or_404(Student, id=id)
    return render(request, "students/db/show.html", {"student": student})





def delete_from_db(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    url = reverse("students.db.index")
    return  redirect(url)
    # return HttpResponse("deleted")



def create(request):
    print(f"request = {request}")
    if request.method == "POST":
        print(request.POST)
        student = Student()
        student.name = request.POST["name"]
        student.email = request.POST["email"]
        student.grade = request.POST["grade"]
        student.image = request.POST["image"]
        student.track = request.POST["track"]
        student.save()  # object contains id from db live
        # url = reverse("students.db.index")
        # return redirect(url)
        url = reverse("students.db.show",args=[student.id])
        return redirect(url)

        # return  HttpResponse("Data received")
    return  render(request, "students/db/create.html")




#### django forms


def create_via_form(request):
    form = StudentForm()  # using django form class
    if request.method == "POST":
        # fill form with request data --> then form will validate the request ??
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            student = Student()
            # student.name = request.POST["name"]
            # student.email = request.POST["email"]
            # student.grade = request.POST["grade"]
            # if "image" in request.FILES:
            #     student.image = request.FILES["image"]
            # student.track = request.POST["track"]  # id

            student.name = form.cleaned_data['name']
            student.email =form.cleaned_data['email']
            student.grade = form.cleaned_data['grade']
            student.image = form.cleaned_data['image']
            student.track = form.cleaned_data['track'] # from cleaned --> get associated related object with the id
            student.gender = form.cleaned_data['gender']
            student.save()  # object contains id from db live
            # url = reverse("students.db.index")
            # return redirect(url)
            url = reverse("students.db.show",args=[student.id])
            return redirect(url)


    return render(request, "students/db/create_form.html", {"form":form})



