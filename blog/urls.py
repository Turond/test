from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.loginp, name='loginp'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^admin/', admin.site.urls),
    #url(r'^login/$',auth_views.login ,{'template_name':'blog/register.html'}, name='login')
]