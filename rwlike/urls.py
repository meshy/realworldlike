from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='home'),
    url(r'^realworldlike/', include('realworldlike.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
