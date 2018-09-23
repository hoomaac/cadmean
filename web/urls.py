from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index, name='index'),
    url(r'^post/$', view=views.post, name='post'),
    url(r'^login/$', view=views.login_user, name='login'),
    url(r'^register/$', view=views.register, name='register'),
    url(r'^logout/$', view=views.logout_user, name='logout'),
    url(r'^stream/$', view=views.stream, name='stream'),
    url(r'^stream/(?P<username>\w+)$', view=views.stream, name='user_stream'),
    url(r'^follow/(?P<username>\w+)$', view=views.follow, name='follow'),
    url(r'^unfollow/(?P<username>\w+)$', view=views.unfollow, name='unfollow'),
    url(r'^delete_post/(?P<post_id>\w+)$', view=views.delete_post, name='delete_post'),
]