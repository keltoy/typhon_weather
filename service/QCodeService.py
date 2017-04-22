#!/usr/bin/env python
import requests
WEATHER_URL = "http://apicloud.mob.com/v1/weather/query"
PM25_URL = "http://apicloud.mob.com/environment/query"
KEY = "1c2506cc3a934"
class QCodeService:
    def requestPM25(self, city):
        params={'key':KEY,'city':city}
        req = requests.get(PM25_URL, params=params)
        if req.status_code == 200:
            return req.json()['result'][0]
        return None

    def requestWeather(self, city):
        params={'key':KEY,'city':city}
        req = requests.get(WEATHER_URL, params=params)
        if req.status_code == 200:
            return req.json()['result'][0]
        return None

