# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from django.db import models


class UrlEntry(models.Model):
    name = models.CharField(max_length=256)


class UrlInfo(models.Model):
    url_entry = models.ForeignKey(UrlEntry)
    version = models.IntegerField()
    url = models.CharField(max_length=4096)
    visible = models.BooleanField()
