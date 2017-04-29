#!/usr/bin/env python
# coding: utf-8

from tornado import gen, web

import logging

log = logging.getLogger('main.base')

class BaseHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        log.warn("error url")
        self.render("error.html")
