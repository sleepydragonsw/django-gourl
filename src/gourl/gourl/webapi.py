# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.views.generic import View

from gourl.gourl.models import Url


class WebApi(View):

    CONTENT_TYPE_JSON = "application/json"

    def post(self, request):
        try:
            response_dict = self._handle_request(request)
        except self.Error as e:
            success = False
            error_message = "{}".format(e)
            response_dict = {"error message": error_message}
        else:
            success = True

        response_dict["success"] = 1 if success else 0
        response_payload = json.dumps(response_dict)
        response = HttpResponse(
            response_payload, content_type=self.CONTENT_TYPE_JSON)
        return response

    class Error(Exception):
        """
        Exception raised by WebApi if an error occurs.
        """
