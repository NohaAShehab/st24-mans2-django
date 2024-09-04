from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    # null on db level , blank= => application
    track = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    grade = models.IntegerField(default=0)
    email = models.EmailField(max_length=100, unique=True, null=True)
    gender = models.Choices('male', 'female')


    # level of the application
    def __str__(self):
        return self.name
