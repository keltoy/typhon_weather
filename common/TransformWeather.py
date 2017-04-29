
# coding: utf-8

import six
import logging
import logging.config


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
    u"冰雹":"lzybybb",
    u"雾":"wu",
    u"霾":"mai"
}


# 1. replace 
# 2. split
# 3. correct
# 

# In[13]:

def replaceBlank(s):
    try:
        s = s.replace('转','-')
        s = s.replace('伴有', '-')
    except Exception as e:
        print(s)
    return s


# In[14]:

def splitWeather(s):
    try:
        begin = s.index('-')
        s = s[begin+1:]
        return s
    except Exception as e:
        return s


# In[15]:

def correctWeather(s):
    try:
        res = WEATHER_ICON_DICT[s]
        if res is not None:
            return res
        if '冰' in res:
            return WEATHER_ICON_DICT['冰雹']
        elif '雷' in res:
            return WEATHER_ICON_DICT['雷阵雨']
        elif '阴' in res:
            return WEATHER_ICON_DICT['阴']
        elif '云' in res:
            return WEATHER_ICON_DICT['多云']
        elif '沙' in res:
            return WEATHER_ICON_DICT['沙尘暴']
        elif '霾' in res:
            return WEATHER_ICON_DICT['霾']
        elif '雨' in res:
            return WEATHER_ICON_DICT['小雨']
        elif '雪' in res:
            return WEATHER_ICON_DICT['小雪']
        elif '晴' in res:
            return WEATHER_ICON_DICT['晴']
        else :
            # add to log
            log.error('cannot find weather')
            return WEATHER_ICON_DICT['晴']
    except Exception as e:
        # add to log
        log.error(e)
        return WEATHER_ICON_DICT['晴']


# In[16]:

def formatWeatherIcon(s):
    s = replaceBlank(s)
    s = splitWeather(s)
    s = correctWeather(s)
    return s

