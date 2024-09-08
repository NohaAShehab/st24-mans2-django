from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/images', null=True, blank=True)
    code = models.CharField(max_length=4, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


