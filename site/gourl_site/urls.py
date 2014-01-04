# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import gourl.gourl.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gourl_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(gourl.gourl.urls, namespace="gourl")),
)
