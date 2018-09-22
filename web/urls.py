from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index, name='index'),
    url(r'^post/$', view=views.post, name='post'),
    url(r'^login/$', view=views.login_user, name='login'),
    url(r'^register/$', view=views.register, name='register'),
    url(r'^logout/$', view=views.logout_user, name='logout'),
    url(r'^stream/(?P<username>\w+)$', view=views.stream, name='user_stream'),
    url(r'^stream/$', view=views.stream, name='stream'),
]