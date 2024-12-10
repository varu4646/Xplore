from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate each blog with a user

    def __str__(self):
        return self.title

