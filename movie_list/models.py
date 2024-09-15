from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title
