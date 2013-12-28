# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class UrlEntry(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class UrlInfo(models.Model):
    url_entry = models.ForeignKey(UrlEntry)
    version = models.IntegerField()
    url = models.CharField(max_length=4096)
    visible = models.BooleanField()

    def __str__(self):
        return self.url
