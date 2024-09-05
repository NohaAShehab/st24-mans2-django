from enum import unique

from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100, required=True)
    track = forms.CharField(label="Track", max_length=100)
    image = forms.CharField(label="Image", max_length=100)
    grade = forms.IntegerField(label="Grade")
    email = forms.EmailField(label="Email", max_length=100, required=True)
    gender = forms.ChoiceField(
        choices=(("male", "Male"), ("female", "Female")),
    )
