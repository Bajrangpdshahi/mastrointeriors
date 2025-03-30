# Create your models here.
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # This will store HTML content
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # New field for the uploaded image
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

