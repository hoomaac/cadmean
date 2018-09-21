from . import models
from django.http import HttpResponse
from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'index.html')
    


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')
    template_name = 'web/login.html'
 
    def get_form(self, form_class = None):
        if form_class is None:
            form_class = self.get_form_class()
        
        return form_class(self.request,**self.get_form_kwargs())  
    

    def form_valid(self, form):
        login(self.request, form.get_user()) 
        return super().form_valid(form)


@login_required
def logout_user(request):
    logout(request)
    return redirect("index")


 
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

