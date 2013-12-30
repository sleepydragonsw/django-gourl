# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse

from gourl.gourl.models import Url
from django.shortcuts import get_object_or_404


def index(request):
    urls = Url.objects.all().order_by("name")
    context = {"urls": urls}
    return render(request, "gourl/index.html", context)


def add(request):
    return HttpResponse("This is the GoUrl add page")


def remove(request, url_id):
    url = get_object_or_404(Url, pk=url_id)
    return HttpResponse(
        "This is the GoUrl remove page for URL: {}".format(url))
