from django import forms
from core.models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name',]