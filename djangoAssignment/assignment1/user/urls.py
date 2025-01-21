from django.urls import path,re_path
from . import views



urlpatterns = [
    re_path("users/",views.allUsers,name="allUsers"),
    re_path(r'^user/(?P<userId>\d+)/$', views.userDetails, name='userDetails'),
    re_path(r'^user/(?P<username>\w+)/$', views.userDetailsByUsername, name='userDetails'),

]
