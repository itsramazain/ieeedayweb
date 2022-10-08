from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .import models
from django.contrib.auth import get_user_model
User=get_user_model()
class PostForm(forms.ModelForm):
    class Meta():
        fields=('group','position','to','massage','stars')
        model=models.Post
        widgits={
        'group':forms.TextInput(attrs={"class":'select'}),
        'position':forms.TextInput(attrs={"class":"position"}),
        'massage':forms.Textarea(attrs={"class":"massage"}),
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['massage'].label = "leave a masssage"
        self.fields['position'].label = "if you are in ieee what is your position?"
        self.fields['group'].label = "you are a "
        self.fields['stars'].label = "rate your IEEE day exporince"
        self.fields['to'].label = "what socity are/were you in"
