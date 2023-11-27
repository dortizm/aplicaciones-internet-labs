from django import forms

class GenreForm(forms.Form):
    genre = forms.ChoiceField(choices=[], required=True)

    def __init__(self, *args, **kwargs):
        genres = kwargs.pop('genres')
        super(GenreForm, self).__init__(*args, **kwargs)
        self.fields['genre'].choices = genres