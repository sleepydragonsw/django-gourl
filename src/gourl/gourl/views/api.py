# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.views.generic import View

from gourl.gourl.models import Url


class WebApi(View):

    CONTENT_TYPE_JSON = "application/json"

    def post(self, request):
        """
        Handles a POST request.
        *request* must be a django.http.HttpRequest object that represents
        the request to fulfill.
        Returns a django.http.HttpResponse object with a JSON payload.
        """
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

    def _handle_request(self, request):
        """
        Processes a request and delegates the action that is requested.
        *request* must be a django.http.HttpRequest object that represents
        the request to fulfill.
        Returns a dictionary that is to be encoded into JSON as the response.
        Raises self.Error if an error occurs.
        """
        self._verify_content_type(request)

    @classmethod
    def _verify_content_type(cls, request):
        """
        Verifies that the "Content-Type" HTTP header is specified and is
        equal to the JSON content type.
        *request* must be a django.http.HttpRequest object whose Content-Type
        HTTP header to verify.
        Raises self.Error if the Content-Type header is not set or is equal
        to an unexpected value.  Returns None otherwise.
        """
        try:
            content_type = request.META["CONTENT_TYPE"]
        except KeyError:
            raise cls.Error("Content-Type HTTP request header missing")
        else:
            if content_type != cls.CONTENT_TYPE_JSON:
                raise cls.Error(
                    "Content-Type HTTP request header has an invalid value: "
                    "{} (expected: {})"
                    .format(content_type, cls.CONTENT_TYPE_JSON))

    class Error(Exception):
        """
        Exception raised by WebApi if an error occurs.
        """
