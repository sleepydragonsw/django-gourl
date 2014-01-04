# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import gourl.urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(gourl.urls, namespace="gourl")),
)
