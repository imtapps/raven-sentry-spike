from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from raven.contrib.django.raven_compat.models import client

client.captureException()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'raven_demo.views.home', name='home'),
    # url(r'^raven_demo/', include('raven_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'', include('sample.urls'))
)
