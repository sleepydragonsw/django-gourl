# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from gourl.gourl.models import UrlEntry
from gourl.gourl.models import UrlInfo

import django.test


class Test_UrlEntry(django.test.TestCase):

    def test_StringRepresentation(self):
        x = UrlEntry(name="blah")
        retval = "{}".format(x)
        self.assertEqual(retval, u"blah")


class Test_UrlInfo(django.test.TestCase):

    def test_StringRepresentation(self):
        x = UrlInfo(url="blah")
        retval = "{}".format(x)
        self.assertEqual(retval, u"blah")
