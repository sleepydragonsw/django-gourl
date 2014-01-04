# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from gourl.gourl.models import Url

import django.test


class Test_Url(django.test.TestCase):

    def test_StringRepresentation(self):
        x = Url(name="foo", url="bar")
        retval = "{}".format(x)
        self.assertEqual(retval, u"foo")

    def test_InitialValues(self):
        x = Url()
        self.assertEqual(x.name, "")
        self.assertEqual(x.url, "")

    def test_Save(self):
        x = Url()
        x.name = "abc"
        x.url = "def"
        x.save()
        url_id = x.id
        url2 = Url.objects.get(pk=url_id)
        self.assertEqual(url2.name, "abc")
        self.assertEqual(url2.url, "def")
