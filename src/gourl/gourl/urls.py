# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import patterns
from django.conf.urls import url

import gourl.gourl.views

urlpatterns = patterns("",
    url(
        r"^$",
        gourl.gourl.views.IndexView.as_view(),
        name="index"),
    url(
        r"^add/$",
        gourl.gourl.views.add,
        name="add"),
    url(
        r"^remove/(?P<url_id>\d+)/$",
        gourl.gourl.views.remove,
        name="remove"),
    url(
        r"^(?P<name>.*)$",
        gourl.gourl.views.redirect,
        name="redirect"),
)
