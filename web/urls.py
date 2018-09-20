from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', view=views.index, name='index'),
    url(r'^login$', view=views.login, name='login'),
    url(r'^register$', view=views.register, name='register'),
]