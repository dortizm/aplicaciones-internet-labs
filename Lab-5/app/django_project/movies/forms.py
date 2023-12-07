from django import forms

class GenreForm(forms.Form):
    genre = forms.CharField(label='Selecciona un género', max_length=100)
