# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.forms.models import ModelForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView

from ..models import Url
from django.shortcuts import render_to_response


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ("name", "url")


class IndexView(ListView):
    queryset = Url.objects.all().order_by("name")


def redirect(request, name):
    url_object = get_object_or_404(Url, name__iexact=name)
    redirect_url = url_object.url
    return HttpResponseRedirect(redirect_url)


def add(request):
    if "submit" in request.POST:
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("gourl:index"))
    else:
        form = UrlForm(request.POST)

    return render(request, "gourl/add.html", {
        "form": form,
        "cancel_redirect_url": reverse("gourl:index"),
    })


def remove(request, url_id):
    url = get_object_or_404(Url, pk=url_id)
    url.delete()
    return HttpResponseRedirect(reverse("gourl:index"))
