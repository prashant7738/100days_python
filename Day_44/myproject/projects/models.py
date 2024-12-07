from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

