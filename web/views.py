from . import models
from django.http import HttpResponse
from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from django.core.urlresolvers import reverse_lazy

class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')
    template_name = 'index.html'

    def get_form(self, form_class = None):
        if form_class is None:
            form_class = self.get_form_class()
        
        return form_class(self.request,**self.get_form_kwargs())

    


def index(request):
    return render(request, 'index.html')
    

def register(request):

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = forms.RegisterForm() 

    return render(request, 'web/register.html', {'form': form})

