from enum import unique

from django import forms
from students.models import Student


class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100, required=True)
    track = forms.CharField(label="Track", max_length=100)
    # image = forms.CharField(label="Image", max_length=100)
    image= forms.ImageField(label="Image", required=False)
    grade = forms.IntegerField(label="Grade")
    email = forms.EmailField(label="Email", max_length=100, required=True)
    gender = forms.ChoiceField(
        choices=(("male", "Male"), ("female", "Female")),
    )

    # define custom validation rule ?
    def clean_email(self):
        email = self.cleaned_data["email"]
        found = Student.objects.filter(email=email).exists()
        if found:
            raise forms.ValidationError("Email already registered before")
        return email


    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters")
        return name
