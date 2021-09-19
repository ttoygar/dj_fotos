from django import forms
from .models import Fotolar


class FotoForm(forms.models.ModelForm):
    class Meta:
        model = Fotolar
        fields = ('notlar', 'user', 'dosya',)

        widgets = {
            'notlar': forms.TextInput(attrs={'size': 30}),
            'user': forms.TextInput(attrs={'size': 30}),
        }
