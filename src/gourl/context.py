# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

"""
A series of template context processors.
"""

from django.conf import settings


def use_cdns(request):
    """
    Adds a "USE_CDNS" context variable whose value is equal to
    settings.USE_CDNS.  This lets templates determine whether or not to
    get third-party CSS and JavaScript libraries, such as JQuery and
    Bootstrap, from the global CDNs or using the locally-hosted versions.
    In production, it is far more efficient to use CDNs, but for development
    it might be easier to use the locally-hosted static versions.
    """
    return {"USE_CDNS": settings.USE_CDNS}
