from django import forms
from django.contrib.admin import widgets

from childapp.apps.children.models import Child

class ChildForm(forms.ModelForm):
    birthday = forms.DateField(widget=widgets.AdminDateWidget())
    class Meta:
        model = Child
        exclude = ['parent']
