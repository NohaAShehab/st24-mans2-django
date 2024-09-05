from django.db import models
from django.shortcuts import  reverse
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    # null on db level , blank= => application
    track = models.CharField(max_length=100, null=True, blank=True)
    # image = models.CharField(max_length=100, null=True, blank=True)
    image=  models.ImageField(upload_to='students/images/', null=True, blank=True)
    grade = models.IntegerField(default=0)
    email = models.EmailField(max_length=100, unique=True, null=True)
    gender = models.Choices('male', 'female')


    # level of the application
    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return f'/media/{self.image}'

    @property
    def show_url(self): # self.id
        url = reverse("students.db.show", args=[self.id])
        return url

    @property
    def delete_url(self):  # self.id
        url = reverse("students.db.delete", args=[self.id])
        return url
