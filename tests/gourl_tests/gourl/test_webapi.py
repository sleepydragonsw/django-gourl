# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import json
import unittest

from gourl.gourl.webapi import WebApi

try:
    from unittest import mock
except ImportError:
    import mock


class Test_WebApi_post(unittest.TestCase):

    def test_RequestIsPassedInToHandleRequest(self):
        x = WebApi()
        x._handle_request = mock.MagicMock(return_value={})
        request = object()
        x.post(request)
        x._handle_request.assert_called_once_with(request)

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
