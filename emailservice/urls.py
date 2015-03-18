from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf.urls import patterns, include, url
from api.api import send_email, send_email_template, email_message_router

from djrill import DjrillAdminSite
admin.site = DjrillAdminSite()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
   # url(r'^', include(email_message_router.urls)),
    url(r'^api-explorer/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^email/send/', send_email),
    url(r'^email/sendtemplate/', send_email_template),
)
