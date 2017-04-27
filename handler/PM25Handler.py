from datetime import datetime
import BaseHandler

class PM2_5Handler(BaseHandler):
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
