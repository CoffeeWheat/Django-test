from django.db import models

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PostPage(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=100)
    sub = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    district = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    seller = models.CharField(max_length=200)
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title