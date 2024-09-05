from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from tracks.models import Track
from tracks.forms import TrackForm


# Create your views here.

def landing(request):
    return render(request, 'tracks/landing.html')



def index(request):
    tracks = Track.objects.all()
    return render(request, 'tracks/index.html', {'tracks': tracks})


def create(request):
    form  = TrackForm()
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            track = Track(name=name, description=description, image=image)
            track.save()
            return  HttpResponse("added")


    return render(request, 'tracks/create.html', {'form': form})



def show(request, id):
    track = get_object_or_404(Track, pk=id)
    return render(request, 'tracks/show.html', {'track': track})
