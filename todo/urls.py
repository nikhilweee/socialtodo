from django.conf.urls import include, url
from todo import views

urlpatterns = [
    url(r'^login/$', views.user_login),
    url(r'^logout/$', views.user_logout),
    url(r'^home/$', views.user_home),
    url(r'^friends/$', views.user_friends),
    url(r'^friends/add/$', views.user_friends_add),
    url(r'^friends/delete/$', views.user_friends_delete),
    url(r'^users/$', views.users_all),
    url(r'^todo/add/$', views.todo_add),
    url(r'^todo/delete/$', views.todo_delete),
    url(r'^todo/completed/$', views.todo_completed),
]
