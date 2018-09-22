from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth import authenticate

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
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = my_model.User
        fields = ('username', 'password')


    def clean(self):
        super().clean()
        username = self.cleaned_data.get('username') 
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError('username or password is incorrect')
        
        return self.cleaned_data


    def login(self, request):
        username = self.cleaned_data.get('username') 
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = my_model.Post
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={'cols':50, 'rows':3, 'class':'form-control',
                                            'placeholder':"what's up?"})
        }


