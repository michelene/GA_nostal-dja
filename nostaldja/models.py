from django.db import models

# Create your models here.
class Decade(models.Model):
    time = models.CharField(max_length = 16)

    def __str__(self):
        return self.time

class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
