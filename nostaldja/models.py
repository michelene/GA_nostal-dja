from django.db import models


class Decade(models.Model):
    start_year = models.CharField(max_length=100)

    def __str__(self):
        return self.start_year


class Fad(models.Model):
    decade = models.ForeignKey(
        Decade, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
