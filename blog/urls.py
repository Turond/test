from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^login/$',auth_views.login ,{'template_name':'blog/register.html'}, name='login')
]