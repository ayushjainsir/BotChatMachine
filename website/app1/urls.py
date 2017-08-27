from django.conf.urls import url
from . import views
from django.contrib.auth.models import User
from django.contrib.auth import login
app_name = 'app1'
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^login/$' , views.login_user , name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^(?P<user_id>[0-9]+)/msgbox/$',views.msgbox, name='msgbox'),
    url(r'^post/$', views.post, name='post'),
    url(r'^messages/$', views.Messages, name='messages'),

]