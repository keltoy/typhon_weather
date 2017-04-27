#!/usr/bin/env python
# coding: utf-8

from tornado import gen, web

class BaseHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render("error.html")
