# encoding:utf-8
from service.QCodeService import QCodeService
from handler.BaseHandler import BaseHandler
from tornado import gen
from common.TransformWeather import formatWeatherIcon

from tornado import gen, web

import logging

log = logging.getLogger('main.qcode')


class QCodeHandler(BaseHandler):
    qCodeService = QCodeService()
    @gen.coroutine
    def get(self, d1):
        #d1 = self.get_argument('d1', '101010100')
        try:
            weather_json = self.qCodeService.requestWeather(d1)
            pm25_json = self.qCodeService.requestPM25(d1)
            hour_data = pm25_json['hourData']
            weather_icon = formatWeatherIcon(weather_json['weather'])
            weather_json['temperature'] = weather_json['temperature'][:-1]
            x = []
            y = []
            for each in hour_data:
                x.insert(0,each['dateTime'])
                y.insert(0,each['aqi'])
            self.render('index.html', w=weather_json, p=pm25_json,x=x,y=y, weather_icon=weather_icon)
        except:
            log.error("qcode error")
            self.render('error.html')
