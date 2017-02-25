#!/usr/bin/env python
# coding: utf-8

from tornado.ioloop import IOLoop
from tornado import gen, web
from common.pm2_5_info import PM2_5Info
from typhoon_weather.crawl_weather import crawlWeather

from tornado_mysql import pools
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime
import configparser

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
    @gen.coroutine
    def get(self):
        delay = self.get_argument('delay', 5)
        yield gen.sleep(int(delay))
        self.write({"status": 1, "msg":"oh success"})
        self.finish()

class PM2_5Handler(web.RequestHandler):
    POOL = pools.Pool(
        connParam,
        max_idle_connections=1,
        max_recycle_sec=3,
    )

    @gen.coroutine
    def post(self):
        d1 = self.get_argument('d1', '101010100')
        now = datetime.now().strftime("%Y_%m_%d_%H")
        time_point = self.get_argument('time_point', now)
        query_id = d1+'_'+ time_point;
        query_id = "101010100_2017_02_24_13"
        cursor =yield self.POOL.execute('select area, d1, time_point, aqi, position_name, station_code, ozone, pm25, pm10, sulfur_dioxide, nitrogen_dioxide, carbonic_oxide, primary_pollutants, air_quality from TB_AQI_CHINA where query_id=%s', query_id)
        code ={}
        if cursor.rowcount > 0:
            code = cursor.fetchone()
            res = PM2_5Info(area=code[0], d1=code[1], time_point=code[2], aqi=code[3], position_name=code[4], station_code=code[5], ozone=code[6], pm25=code[7], pm10=code[8], sulfur_dioxide=code[9], nitrogen_dioxide=code[10], carbonic_oxide=code[11], primary_pollutants=code[12], air_quality=code[13])
        self.write(res.to_json())
        self.finish()



class WeatherHandler(web.RequestHandler):
    POOL = pools.Pool(
        connParam,
        max_idle_connections=1,
        max_recycle_sec=3,
    )

    @gen.coroutine
    def post(self):
        code = ""
        d2 = self.get_argument('d2')
        d4 = self.get_argument('d4')
        cursor = yield self.POOL.execute('select d1 from tb_city_info_china where d2=%s and d4=%s', (d2,d4))
        if cursor.rowcount > 0:
            code = cursor.fetchone()[0]

        url = URL % code
        client = AsyncHTTPClient()
        response = yield client.fetch(url, method='GET')
        res = crawlWeather(response.body)
        self.finish(res.to_json())


application = web.Application([
    (r"/", MainHandler),
    (r"/weather", WeatherHandler),
    (r"/pm2_5", PM2_5Handler)
    ], autoreload=True)
application.listen(8000)
IOLoop.current().start()


# In[ ]:



