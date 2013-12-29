from django.conf.urls import patterns, url

from pasosbaile import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index')
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^bailes/$', views.bailes_index, name='bailes'),
    url(r'^(?P<dance_name>\w+)/$', views.tipo_baile_index, name='tipo_baile_index'),
    url(r'^(?P<dance_name>\w+)/(?P<step_id>\d+)/$', views.paso_baile_detalle, name='paso_baile_detalle'),
)