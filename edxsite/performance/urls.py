from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<week_id>[0-9]+)/results/$', views.week_detail, name='week_detail'),
]