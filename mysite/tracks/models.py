from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Track(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField( upload_to='tracks/images',null=True, blank=True)
    # fill this field when object created
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # fill this field when object update
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return f'/media/{self.image}'


    @property
    def show_url(self):
        url = reverse('tracks.show', args=[self.id])
        return url


