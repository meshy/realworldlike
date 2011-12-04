from django.conf.urls.defaults import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from realworldlike.models import PrintRun, Spot
from realworldlike.views import SpotCreateView, PrintRunCreateView, PrintRunJSONView



urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='realworldlike/rwl_index.html'), name='rwl_index'),
    url(r'^printrun/$', ListView.as_view(model=PrintRun), name='printrun_list'),
    url(r'^printrun/new/$', PrintRunCreateView.as_view(), name='printrun_create'),
    url(r'^printrun/(?P<pk>\d+)/$', PrintRunJSONView.as_view(), name='printrun_json'),
    url(r'^spot/$', ListView.as_view(model=Spot), name='spot_list'),
    url(r'^spot/(?P<pk>\d+)/$', DetailView.as_view(model=Spot), name='spot_detail'),
    url(r'^spot/new/$', csrf_exempt(SpotCreateView.as_view())),
)
