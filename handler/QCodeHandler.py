# encoding:utf-8
from service.QCodeService import QCodeService
from handler.BaseHandler import BaseHandler
from tornado import gen

WEATHER_ICON_DICT = { 
    u"中雨":"zhongyu",
    u"中雨转大雨":"zyzdy",
    u"中雪":"zhongxue",
    u"中雪转大雪":"zxzdx",
    u"冻雨":"dongyu",
    u"多云":"duoyun",
    u"大暴雨":"dby",
    u"大暴雨转特大暴雨":"dbyztdby",
    u"大雨":"dayu",
    u"大雨转暴雨":"dyzby",
    u"大雪":"daxue",
    u"大雪转暴雪":"dxzbx",
    u"小雨":"xiaoyu",
    u"小雨转中雨":"xyzzy",
    u"小雪":"xiaoxue",
    u"小雪转中雪":"xxzzx",
    u"扬沙":"yangsha",
    u"晴":"qing",
    u"暴雨":"baoyu",
    u"暴雨转大暴雨":"byzdby",
    u"暴雪":"baoxue",
    u"沙尘暴":"scb",
    u"浮尘":"fuchen",
    u"特大暴雨":"tdby",
    u"特强沙尘暴":"tqscb",
    u"阴":"yin",
    u"阵雨":"zhenyu",
    u"阵雪":"zhenxue",
    u"雨夹雪":"yjx",
    u"雷阵雨":"lzy",
    u"雷阵雨伴有冰雹":"lzybybb",
    u"雾":"wu",
    u"霾":"mai"
}


class QCodeHandler(BaseHandler):
    qCodeService = QCodeService()
    @gen.coroutine
    def get(self, d1):
        #d1 = self.get_argument('d1', '101010100')
        weather_json = self.qCodeService.requestWeather(d1)
        pm25_json = self.qCodeService.requestPM25(d1)
        hour_data = pm25_json['hourData']
        weather_icon = WEATHER_ICON_DICT[weather_json['weather']]
        x = []
        y = []
        for each in hour_data:
            x.insert(0,each['dateTime'])
            y.insert(0,each['aqi'])
        self.render('index.html', w=weather_json, p=pm25_json,x=x,y=y, weather_icon=weather_icon)
