from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf.urls import patterns, include, url
from api.api import send_email


from djrill import DjrillAdminSite
admin.site = DjrillAdminSite()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emailservice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^', include(email_router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sendemail', send_email),
    #url(r'^sendemailtemplate', send_email_template)
    #url(r'^emails', get_emails),
    #url(r'^email/send', send_email),
    #url(r'^admin/', include(admin.site.urls)),
)
