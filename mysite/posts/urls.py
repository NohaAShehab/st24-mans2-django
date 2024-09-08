
from django.urls import path
from posts.views import  create, PostView, CreatePost, edit, UpdatePost, DeletePost, PostListView, PostDetailView
urlpatterns = [

    # path('create',create, name='posts.create' ),
    # path('', PostView.as_view(), name='posts.index'),
    path('create/', CreatePost.as_view(), name='posts.create'),
    # path('posts/<int:id>/edit', edit, name='posts.edit'),
    path('posts/<int:pk>/edit',UpdatePost.as_view(), name='posts.edit' ),
    path('posts/<int:pk>/delete',DeletePost.as_view(), name='posts.delete'),
    path('', PostListView.as_view(), name='posts.index'),
    path('<int:pk>', PostDetailView.as_view(), name='posts.show'),


]