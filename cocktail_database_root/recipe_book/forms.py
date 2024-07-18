from django import forms


class GetSelection(forms.Form):
    name = forms.CharField(max_length=80)
    ingredient = forms.CharField(max_length=80, required=False)