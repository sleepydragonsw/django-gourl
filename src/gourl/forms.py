# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from gourl.models import Url

from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.bootstrap import FormActions
from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.helper import Layout
from crispy_forms.layout import Submit
from crispy_forms.layout import Field
from crispy_forms.layout import Div
from crispy_forms.layout import HTML


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

    helper = FormHelper()
    helper.form_class = "form-horizontal"
    helper.label_class = "col-lg-2"
    helper.field_class = "col-lg-8"
    helper.layout = Layout(
        HTML("<div class='col-lg-2'></div><h2>Add URL</h2>"),
        PrependedText("name", "go/", placeholder="google"),
        Field("url", placeholder="http://www.google.com"),
        Div(css_class="col-lg-2"),
        FormActions(
            Submit("submit", _("Add URL")),
        ),
    )
