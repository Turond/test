from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$',auth_views.login ,{'template_name':'blog/login_page.html'}, name='login')
    #, {'template_name':'blog/login_page.html'}),
]