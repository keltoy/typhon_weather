#!/usr/bin/env python
# coding: utf-8

from tornado.ioloop import IOLoop
from tornado import gen, web
from common.item import Item
from typhoon_weather.crawl_weather import crawlWeather
from service.QCodeService import QCodeService
from tornado_mysql import pools
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime
from handler.BaseHandler import BaseHandler
from handler.HomeHandler import HomeHandler
from handler.QCodeHandler import QCodeHandler
import ujson
import configparser
import os
from tornado.httpserver import HTTPServer

# monkey patch
json = ujson

cp = configparser.ConfigParser()
cp.read("resource.conf")
host = cp.get('db', 'db_host')
port = cp.get('db', 'db_port')
user = cp.get('db', 'db_user')
passwd = cp.get('db', 'db_passwd')
db = cp.get('db', 'db_name')
charset = cp.get('db', 'db_charset')
connParam = {'host':host, 'port':int(port), 'user':user, 'passwd':passwd,'db': db, 'charset':charset}
URL = "http://www.weather.com.cn/weather1d/%s.shtml"

class Application(web.Application):
    def __init__(self):
        handlers= [(r"/",HomeHandler),
                   (r"/propagation/([%a-fA-F0-9]+)", QCodeHandler),
                   (r".*", BaseHandler)
        ]
        template_path=os.path.join(os.path.dirname(__file__), "templates")
        static_path=os.path.join(os.path.dirname(__file__), "static")
        self.db = pools.Pool(connParam, max_idle_connections=5, max_recycle_sec=3)
        web.Application.__init__(self,
                                 handlers=handlers,
                                 autoreload=True,
                                 template_path=template_path,
                                 static_path=static_path
                                 )


if __name__ == "__main__":
    http_server = HTTPServer(Application())
    http_server.listen(8000)
    IOLoop.current().start()
