# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from gourl.gourl.models import Url

import django.test


class Test_Url(django.test.TestCase):

    def test_StringRepresentation(self):
        x = Url(name="foo", url="bar")
        retval = "{}".format(x)
        self.assertEqual(retval, u"foo")
