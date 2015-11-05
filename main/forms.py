from django import forms
from .models import Loyaltycodes2

class Upload_Form(forms.Form):
    filespec = forms.FileField()
