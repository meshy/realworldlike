from django.conf.urls.defaults import patterns, include, url
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from realworldlike.models import Spot
from realworldlike.views import SpotCreateView, PrintRunCreateView
from realworldlike.forms import SpotForm


urlpatterns = patterns('',
    #url(r'^$', ListView.as_view(model=PrintRun), name='home'),
    url(r'^spot/$', ListView.as_view(model=Spot), name='spot_list'),
    url(r'^spot/(?P<pk>\d+)$', DetailView.as_view(model=Spot), name='spot_detail'),
    url(r'^spot/new/$', SpotCreateView.as_view(form_class=SpotForm)),
)
