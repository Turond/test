from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.login, name='loginp'),
    url(r'^login/$', auth_views.login, {'template_name': 'blog/loginp.html'}, name='loginp'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^admin/', admin.site.urls),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'registration/password_reset_form.html'},
        name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
    #url(r'^login/$',auth_views.login ,{'template_name':'blog/register.html'}, name='login')
]