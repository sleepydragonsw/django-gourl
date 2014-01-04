# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import unittest

from django.test import TestCase
from django.test.client import RequestFactory

from gourl.views.api import WebApi

try:
    from unittest import mock
except ImportError:
    import mock


class Test_WebApi_post(unittest.TestCase):

    # verify that the request object is passed on to _handle_request()
    def test_RequestIsPassedInToHandleRequest(self):
        x = WebApi()
        x._handle_request = mock.MagicMock(return_value={})
        request = object()
        x.post(request)
        x._handle_request.assert_called_once_with(request)

    # verify the HTTP response when _handle_request() succeeds
    def test_HandleRequestSuccess(self):
        x = WebApi()
        x._handle_request = mock.MagicMock(return_value={"one": "two"})
        response = x.post(object())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        response_dict = json.loads(response.content.decode())
        self.assertDictEqual(response_dict, {
            "one": "two",
            "success": 1,
        })

    # verify the HTTP response when _handle_request() fails
    def test_HandleRequestError(self):
        x = WebApi()
        exception = x.Error("forced exception")
        x._handle_request = mock.MagicMock(side_effect=exception)
        response = x.post(object())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        response_dict = json.loads(response.content.decode())
        self.assertDictEqual(response_dict, {
            "success": 0,
            "error message": "forced exception",
        })


class Test_WebApi__verify_content_type(TestCase):

    def test_Success(self):
        x = WebApi()
        request = self.new_request(content_type="application/json")
        retval = x._verify_content_type(request)
        self.assertIsNone(retval)

    def test_Error_ContentTypeIsIncorrectCase(self):
        self.do_test_error(content_type="Application/JSON")

    def test_Error_ContentTypeIsIncorrect(self):
        self.do_test_error(content_type="text/plain")

    def test_Error_ContentTypeIsNotSpecified(self):
        request = self.new_request()
        del request.META["CONTENT_TYPE"]
        self.do_test_raises_error(
            request=request,
            expected_message="Content-Type HTTP request header missing",
        )

    def do_test_error(self, content_type):
        request = self.new_request(content_type=content_type)
        self.do_test_raises_error(
            request=request,
            expected_message="Content-Type HTTP request header has an invalid "
                "value: {} (expected: application/json)".format(content_type),
        )

    def do_test_raises_error(self, request, expected_message):
        x = WebApi()
        with self.assertRaises(x.Error) as cm:
            x._verify_content_type(request)
        actual_message = "{}".format(cm.exception)
        self.assertEqual(actual_message, expected_message)

    def new_request(self, **kwargs):
        factory = RequestFactory()
        request = factory.post("/", **kwargs)
        return request
