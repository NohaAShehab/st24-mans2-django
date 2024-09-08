from django.db import models
from django.shortcuts import  redirect, reverse
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/images', null=True, blank=True)
    code = models.CharField(max_length=4, null=True, blank=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='posts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


    @property
    def image_url(self):
        return f'/media/{self.image}'


    @property
    def edit_url(self):
        url = reverse('posts.edit',args=[self.id])
        return url

    @property
    def delete_url(self):
        url = reverse('posts.delete', args=[self.id])
        return url

    @property
    def show_url(self):
        url = reverse('posts.show', args=[self.id])
        return url

