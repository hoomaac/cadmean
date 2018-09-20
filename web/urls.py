from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', view=views.login, name='login')
]