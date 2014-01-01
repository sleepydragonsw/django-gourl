# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse

from gourl.gourl.models import Url
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
import django.views.generic


class IndexView(django.views.generic.ListView):
    queryset = Url.objects.all().order_by("name")


def redirect(request, name):
    url_object = get_object_or_404(Url, name__iexact=name)
    redirect_url = url_object.url
    return HttpResponseRedirect(redirect_url)


def add(request):
    context = {}
    if "cancel" in request.POST:
        return HttpResponseRedirect(reverse("gourl:index"))
    elif "submit" in request.POST:
        try:
            request.POST["submit"]
            name = request.POST["name"]
            url = request.POST["url"]
        except KeyError:
            pass
        else:
            context["name"] = name
            context["url"] = url
            name = name.strip()
            url = url.strip()

            if len(name) == 0 or len(url) == 0:
                context["error"] = "Both name and URL must be specified"
            else:
                url_object = Url(name=name, url=url)
                url_object.save()
                return HttpResponseRedirect(reverse("gourl:index"))

    return render(request, "gourl/add.html", context)


def remove(request, url_id):
    url = get_object_or_404(Url, pk=url_id)
    return HttpResponse(
        "This is the GoUrl remove page for URL: {}".format(url))
