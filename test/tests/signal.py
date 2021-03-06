#encoding:utf8

from contextlib import contextmanager

from . import ClientTest
from .. import requests
from ..app import app, wechat
from ..context import signal_context as context

import flask_wechat.signals as signals

class SignalTestCases(ClientTest):
    token = "123456"

    def setUp(self):
        super(SignalTestCases, self).setUp()
        app.config["id"] = self.identity
        app.config["token"] = self.token
        # app.config["WECHAT_DEBUG"] = True
        # app.config["DEBUG"] = True
        self.app = app.test_client()
        wechat.init_app(app)
        self.posturl = wechat.callback_prefix +  "/" + self.identity + "/"
        
    def test_1_response_sent(self):
        with context(signals.response_sent, wechat) as records:
            resp = self.create_request(requests.image)
            self.__record_verify(records)
            self.assertTrue(records[0]["identity"]==self.identity)
            self.assertTrue(records[0]["response"].content == "image")
            
        with context(signals.response_sent, wechat) as records:
            resp = self.create_request(requests.badrequest)
            self.__record_verify(records, 0)
            
        with context(signals.response_sent, wechat) as records:
            resp = self.create_request(requests.exception)
            self.__record_verify(records, 1)
            self.assertTrue(records[0]["identity"]==self.identity)
            self.assertTrue(records[0]["response"] == "")
    
    def __record_verify(self, records, length=1):
        self.assertTrue(len(records)==length)