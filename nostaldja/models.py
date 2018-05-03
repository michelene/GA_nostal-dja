from django.db import models

# Create your models here.
class Decade(models.Model):
    time = models.CharField(max_length = 16)

class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='decades')
    title = models.CharField(max_length=100)
    description = models.TextField()
