from django import forms

class Numero(forms.Form):
    numero = forms.IntegerField()