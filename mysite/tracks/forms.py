

from django import forms
from tracks.models import Track

class TrackForm(forms.Form):
    name = forms.CharField(
        label='Track name',
        max_length=100,
        )

    image = forms.ImageField(
        # widget=forms.FileInput(attrs={'class': 'form-control'}),
                             label='Track image', required=False)

    description = forms.CharField(
        # widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  label='Track description', required=False)


    def clean_name(self):
        name = self.cleaned_data['name']
        track_name = Track.objects.filter(name=name).exists()
        if track_name:
            raise forms.ValidationError("Track with this name already exists")
        return name

