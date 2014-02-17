# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from gourl.models import Url


class AddUrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ["name", "url"]
        labels = {
            "name": _("Name"),
            "url": _("URL"),
        }
        help_texts = {
            "name": _("The name of the URL"),
            "url": _("The full URL to which the name should redirect"),
        }
