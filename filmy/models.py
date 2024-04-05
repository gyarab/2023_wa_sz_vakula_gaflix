from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=256)
    year = models.PositiveSmallIntegerField(blank= True, null= True)
    footage = models.PositiveSmallIntegerField(blank=True, null = True, help_text= "in minutes")

    def __str__(self):
        return self.title
