# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from gourl.forms import AddUrlForm
from gourl.models import Url

from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy


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

    def get(self, request, *args, **kwargs):
        return super(AddUrlView, self).get(request, *args, **kwargs)


def remove(request, url_id):
    url = get_object_or_404(Url, pk=url_id)
    url.delete()
    return HttpResponseRedirect(reverse("gourl:index"))
