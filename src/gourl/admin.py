# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.contrib import admin

from .models import Url


class UrlAdmin(admin.ModelAdmin):
    fields = ["name", "url"]
    list_display = ["name", "url"]
    search_fields = ["name", "url"]

admin.site.register(Url, UrlAdmin)
