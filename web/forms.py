from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms 

from . import models as my_model

class RegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'username', 'class':'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder':'email','class':'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder':'password', 'class':'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder':'confirm password', 'class':'form-control'})


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    # class Meta:
    #     model = get_user_model()
    #     fields = ('username', 'password')


class PostForm(forms.ModelForm):
    class Meta:
        model = my_model.Post
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={'cols':50, 'rows':4, 'class':'form-control'})
        }


