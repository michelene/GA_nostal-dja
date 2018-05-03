from django.contrib import admin
from nostaldja.models import Decade, Fad

# Register your models here.
admin.site.register([Decade, Fad])
