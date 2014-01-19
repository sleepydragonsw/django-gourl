# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Url(models.Model):

    name = models.CharField(max_length=256)
    url = models.URLField(max_length=4096)

    def __str__(self):
        return self.name
