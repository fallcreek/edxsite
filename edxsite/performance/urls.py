from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^week_performance/$', views.week_list, name='week_list'),
    url(r'^Week(?P<week_id>[0-9]+)/$', views.problem_list, name='problem_list'),
]