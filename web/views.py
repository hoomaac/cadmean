from . import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib import messages
from django.utils.decorators import method_decorator

from . import forms as my_form
from . import models as my_model


def index(request):
    return render(request, 'index.html')
    


# class LoginView(generic.FormView):
#     form_class = AuthenticationForm
#     success_url = reverse_lazy('index')
#     template_name = 'web/login.html'
 
    # def get_form(self, form_class = None):
    #     if form_class is None:
    #         form_class = self.get_form_class()
        
    #     return form_class(self.request,**self.get_form_kwargs())  


    # @method_decorator(csrf_protect)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(LoginView, self).dispatch(request, *args, **kwargs)
    
    # def form_valid(self, form):
    #     messages.success(self.request, 'logged in')
    #     login(self.request, form.get_user()) 
    #     return super().form_valid(form)


    # def set_test_cookie(self):
    #     self.request.session.set_test_cookie()


    # def get(self, request, *args, **kwargs):

    #     self.set_test_cookie()
    #     return super(LoginView, self).get(request, *args , **kwargs)


    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     if form.is_valid():
    #         return self.form_valid(form)

    #     else:
    #         self.set_test_cookie()
    #         return self.form_invalid(form)


def login_user(request):
    form = my_form.LoginForm(request.POST or None)

    
    if request.POST and form.is_valid():
        print('login im here')
        user = form.login(request)

        if user:
            login(request, user)
            return redirect('index')

        else:
            messages.error(request, "user dones't exist")
            return redirect(request, 'index')
    
    return render(request, 'web/login.html', {'form':form})
    

    
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

    if request.method == 'POST':
        form = my_form.PostForm(request.POST)
        
        if form.is_valid():
            post_obj = form.save(commit=False)
            post_obj.user = request.user
            post_obj.save()
            
            messages.success(request, 'posted')
            return redirect('index')
        else:
            
            messages.error(request, 'wrong')
            return redirect('post')
    else:
        form = my_form.PostForm()
    
    return render(request, 'web/post.html', {'form':form})
        

        
#TODO: make stream view for users and global to see posts
#TODO: make templates for stream

@login_required
def stream(request, username=None):

    template_name = 'web/stream.html'
    
    if username and username != request.user.username:
        user = my_model.User.objects.get(username=username)
        if user:
            stream = user.posts.all().order_by('-id')[:10]
        
    else:
        stream = request.user.get_stream()
        user = request.user
        print('user does not exist')

    if username:
        template_name = 'web/user_stream.html'

    return render(request, template_name, {'stream':stream, 'user':user})


# @login_required
# def user_stream(request, username):

#     return render(request, 'web/user_stream.html', {'username':username})