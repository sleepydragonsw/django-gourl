# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from gourl.forms import AddUrlForm
from gourl.models import Url

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.views.generic import ListView


class IndexView(ListView):
    queryset = Url.objects.all().order_by("name")


def redirect(request, name):
    url_object = get_object_or_404(Url, name__iexact=name)
    redirect_url = url_object.url
    return HttpResponseRedirect(redirect_url)


class AddUrlView(CreateView):
    form_class = AddUrlForm
    success_url = reverse_lazy("gourl:index")
    template_name = "gourl/add.html"

    def get_context_data(self, **kwargs):
        form = kwargs["form"]
        initially_focussed_field = self._field_for_initial_focus(form)
        return super(AddUrlView, self).get_context_data(
            initially_focussed_field=initially_focussed_field,
            **kwargs)

    def _field_for_initial_focus(self, form):
        fields = form.visible_fields()
        for field in fields:
            if field.name in form.errors:
                return field
        return fields[0]


def remove(request, url_id):
    url = get_object_or_404(Url, pk=url_id)
    url.delete()
    return HttpResponseRedirect(reverse("gourl:index"))
