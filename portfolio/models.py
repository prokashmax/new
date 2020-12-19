from django.db import models

# Create your models here.
class project(models.Model):
    titel = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.titel