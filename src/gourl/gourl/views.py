# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from django.template import RequestContext
from django.template import loader
from django.http.response import HttpResponse

from gourl.gourl.models import Url


def index(request):
    urls = Url.objects.all().order_by("name")
    template = loader.get_template("gourl/index.html")
    context = RequestContext(request, {
        "urls": urls,
    })
    return HttpResponse(template.render(context))


def add(request):
    return HttpResponse("This is the GoUrl add page")


def remove(request, url_id):
    return HttpResponse("This is the GoUrl remove page")
