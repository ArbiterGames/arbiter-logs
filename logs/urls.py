from django.conf.urls import patterns, include, url
from django.contrib import admin
from logs.views import ReportingHandler

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^report$', ReportingHandler.as_view(), name='report'),
)
