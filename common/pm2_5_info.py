import ujson

class PM2_5Info(object):
    """
    aqi	空气质量指数(AQI)，即air quality index，是定量描述空气质量状况的无纲量指数
    area	城市名称
    position_name	监测点名称
    station_code	监测点编码
    so2	二氧化硫1小时平均
    so2_24h	二氧化硫24小时滑动平均
    no2	二氧化氮1小时平均
    no2_24h	二氧化氮24小时滑动平均
    pm10	颗粒物（粒径小于等于10μm）1小时平均
    pm10_24h	颗粒物（粒径小于等于10μm）24小时滑动平均
    co	一氧化碳1小时平均
    co_24h	一氧化碳24小时滑动平均
    o3	臭氧1小时平均
    o3_24h	臭氧日最大1小时平均
    o3_8h	臭氧8小时滑动平均
    o3_8h_24h	臭氧日最大8小时滑动平均
    pm2_5	颗粒物（粒径小于等于2.5μm）1小时平均
    pm2_5_24h	颗粒物（粒径小于等于2.5μm）24小时滑动平均
    primary_pollutant	首要污染物
    quality	空气质量指数类别，有“优、良、轻度污染、中度污染、重度污染、严重污染”6类
    time_point	数据发布的时间
    """
    def __init__(self, **args):
        self.args = args

    def to_json(self):
        return ujson.dumps(self.args)
