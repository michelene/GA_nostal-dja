from django import forms
from .models import Decade, Fad

class DecadeForm(forms.ModelForm):

    class Meta:
        model = Decade
        fields = ('time',)

class FadForm(forms.ModelForm):

    class Meta:
        model = Fad
        fields = ('decade', 'title', 'description')
