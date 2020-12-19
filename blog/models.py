from django.db import models

# Create your models here.
class blogs(models.Model):
    titel = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='blog/images')
    date = models.DateField()

    def __str__(self):
        return self.titel