from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index, name='index'),
    # url(r'^index/$', view=views.index, name='index'),
    url(r'^login/$', view=views.LoginView.as_view(), name='login'),
    url(r'^register/$', view=views.register, name='register'),
    url(r'^logout/$', view=views.logout_user, name='logout'),
]