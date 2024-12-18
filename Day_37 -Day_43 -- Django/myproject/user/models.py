from django.db import models

# Create your models here.
class User(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default = 'fullback.png' ,blank=True)

    def __str__(self):
        return self.title

