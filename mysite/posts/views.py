from django.shortcuts import render
from django.http import  HttpResponse
from posts.forms import  PostForm

# Create your views here.

def create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save() # create object directly
            return  HttpResponse("post saved")

    return render(request, 'posts/create.html', {'form': form})
