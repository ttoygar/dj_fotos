from django import forms
from .models import Fotolar


# class ItemForm(forms.models.ModelForm):
#     class Meta:
#         model = Fotolar
#         fields = ('notlar',)
    # item = forms.CharField(
    #     widget=forms.fields.TextInput(attrs={
    #         'placeholder':'Enter text',
    #     }),
    # )

class FotoForm(forms.models.ModelForm):
    # tarih = forms.DateTimeField()
    # notlar = forms.Textarea()
    # user = forms.CharField(max_length=50)
    # dosya = forms.ImageField()

    class Meta:
        model = Fotolar
        fields = ('notlar','user','dosya',)

        widgets = {

            'notlar': forms.TextInput(attrs={'size': 120}),
            'user': forms.TextInput(attrs={'size': 120}),

        }
