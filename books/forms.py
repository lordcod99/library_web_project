from django import forms
from django.db import models
from django.forms import fields
from django.forms.models import ModelFormMetaclass
from comments.models import comment
# creating a form 
class review_form(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comment']
    