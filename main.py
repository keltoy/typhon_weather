#!/usr/bin/env python
# coding: utf-8

from tornado.ioloop import IOLoop
from tornado import gen, web
from common.item import Item
from typhoon_weather.crawl_weather import crawlWeather

from tornado_mysql import pools
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime
import configparser
import os

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

class MainHandler(web.RequestHandler):
    POOL = pools.Pool(connParam, max_idle_connections=5, max_recycle_sec=3)
    @gen.coroutine
    def get(self):
        delay = self.get_argument('delay', 5)
        yield gen.sleep(int(delay))
        self.write({"status": 1, "msg":"oh success"})
        self.finish()

class PM2_5Handler(web.RequestHandler):
    POOL = pools.Pool(connParam, max_idle_connections=5, max_recycle_sec=3)
    @gen.coroutine
    def post(self):
        d1 = self.get_argument('d1', '101010100')
        now = datetime.now().strftime("%Y_%m_%d_%H")
        time_point = self.get_argument('time_point', now)
        query_id = d1+'_'+ time_point;
        query_id = "101010100_2017_02_24_13"
        cursor =yield self.POOL.execute('select area, d1, time_point, aqi, position_name, station_code, ozone, pm25, pm10, sulfur_dioxide, nitrogen_dioxide, carbonic_oxide, primary_pollutants, air_quality from TB_AQI_CHINA where query_id=%s', query_id)
        if cursor.rowcount > 0:
            code = cursor.fetchone()
            res = Item(area=code[0], d1=code[1], time_point=code[2], aqi=code[3], position_name=code[4], station_code=code[5], ozone=code[6], pm25=code[7], pm10=code[8], sulfur_dioxide=code[9], nitrogen_dioxide=code[10], carbonic_oxide=code[11], primary_pollutants=code[12], air_quality=code[13])
        self.write(res.to_json())
        self.finish()



class WeatherDayHandler(web.RequestHandler):
    POOL = pools.Pool(connParam, max_idle_connections=5, max_recycle_sec=3)
    @gen.coroutine
    def get(self, d1, time):
        query_id_day = d1 +'_' + time[:-3]
        query_id_hour = d1 +'_' + time
        sql_day = 'select d1, time_point, area, temperature_max, temperature_min, humidity_max, humidity_min, weather, wind, special_sign from TB_WEATHER_DAY_CHINA where query_id=%s'
        sql_hour = 'select temperature, humidity, wind, weather from TB_WEATHER_HOUR_CHINA where query_id=%s'
        cursor = yield self.POOL.execute(sql_day,query_id_day)
        if cursor.rowcount > 0:
            code = cursor.fetchone()
            res = Item(d1=code[0], time_point=code[1], area=code[2], temperature_max=code[3], temperature_min=code[4], humidity_max=code[5], humidity_min=code[6], weather=code[7], wind=code[8], special_sign=code[9]).to_json()
        else:
            res = {"area": "北京"}

        cursor = yield self.POOL.execute(sql_hour,query_id_hour)
        if cursor.rowcount > 0:
            code = cursor.fetchone()
            res['temperature']=code[0]
            res['humidity'] = code[1]
            res['wind'] = code[2]
            res['weather'] = code[3]
        self.write(res)
        self.finish()


class QCodePageHandler(web.RequestHandler):
    @gen.coroutine
    def get(self, d1):
        self.render('index.html')


application = web.Application(handlers=[
    (r"/", MainHandler),
    (r"/weather/(\w+)/(\w+)", WeatherDayHandler),
    (r"/pm2_5", PM2_5Handler),
    (r"/propagation/(\w+)", QCodePageHandler)
    ],
                              autoreload=True,
                              template_path=os.path.join(os.path.dirname(__file__), "templates"),
                              static_path=os.path.join(os.path.dirname(__file__), "static")
)
application.listen(8000)
IOLoop.current().start()


# In[ ]:



