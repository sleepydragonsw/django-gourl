# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import patterns
from django.conf.urls import url

from .views.api import WebApi
from .views.ui import AddUrlView
from .views.ui import remove as remove_view
from .views.ui import redirect as redirect_view
from .views.ui import IndexView

urlpatterns = patterns(
    "",
    url(
        r"^$",
        IndexView.as_view(),
        name="index"),
    url(
        r"^actions/add/$",
        AddUrlView.as_view(),
        name="add"),
    url(
        r"^actions/remove/(?P<url_id>\d+)/$",
        remove_view,
        name="remove"),
    url(
        r"^actions/api/$",
        WebApi.as_view(),
        name="api"),
    url(
        r"^(?P<name>.*)$",
        redirect_view,
        name="redirect"),
)
