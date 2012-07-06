from django import forms

from childapp.apps.children.models import Child

class ChildForm(forms.ModelForm):

    class Meta:
        model = Child
        exclude = ['parent']
