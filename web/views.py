from . import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib import messages


from . import forms as my_form



def index(request):
    return render(request, 'index.html')
    


# class LoginView(generic.FormView):
    # form_class = AuthenticationForm
    # success_url = reverse_lazy('index')
    # template_name = 'web/login.html'
 
    # def get_form(self, form_class = None):
    #     if form_class is None:
    #         form_class = self.get_form_class()
        
    #     return form_class(self.request,**self.get_form_kwargs())  
    
    # def form_valid(self, form):
    #     login(self.request, form.get_user()) 
    #     return super().form_valid(form)

def login_user(request):
    
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            #TODO: error message should be printed
            
            return redirect('login')
        else:
            #TODO: success message should be printed 
            login(request, user)
            return redirect('index')

    else:
        form = my_form.LoginForm() 

    return render(request, 'web/login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect("index")


 
def register(request):

    if request.method == 'POST':
        form = my_form.RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = my_form.RegisterForm() 

    return render(request, 'web/register.html', {'form': form})


@login_required
def post(request):

    user = request.user
    if request.method == 'POST':
        form = my_form.PostForm(request.POST)
        
        if form.is_valid():
            post_obj = form.save(commit=False)
            post_obj.user = request.user
            post_obj.save()
            
            print(form.cleaned_data.get('content'))
            messages.success(request, 'posted')
            return redirect('post')
        else:
            print('failed')
            print(request.user)
            messages.error(request, 'wrong')
            return redirect('post')
    else:
        form = my_form.PostForm()
    
    return render(request, 'web/post.html', {'form':form})
        

        