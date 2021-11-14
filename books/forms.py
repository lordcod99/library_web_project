from django import forms
from django.db import models
from django.forms import fields
from django.forms.models import ModelFormMetaclass
from comments.models import comment
# creating a form 

class search_form(forms.Form):
    search = forms.CharField(max_length=100)
    
class review_form(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comment']
    