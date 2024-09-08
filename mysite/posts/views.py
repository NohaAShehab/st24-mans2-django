from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import  HttpResponse
from posts.forms import  PostForm
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import  ListView, DetailView

from posts.models import Post


# Create your views here.

def create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save() # create object directly
            return  HttpResponse("post saved")

    return render(request, 'posts/create.html', {'form': form})


def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # update instance object with new data
            post = form.save()
            url = reverse('posts.index')
            return redirect(url)

    return render(request, 'posts/edit.html', {'form': form})



# class based views ??

class PostView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'posts/index.html', {'posts': posts})




# class based views

# class CreatePost(View):
#     def get(self, request, *args, **kwargs):
#         form = PostForm()
#         return render(request, 'posts/create.html', {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save()
#             url = reverse('posts.index')
#             return redirect(url)



### generic views ??

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = "/posts"


# edit view with generic views ?

class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/edit.html'
    success_url = "/posts"


class DeletePost(DeleteView):
    model = Post
    success_url = "/posts"


class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/show.html'
    context_object_name = 'post'










