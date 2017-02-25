import bs4
import requests

URL = "http://www.weather.com.cn/weather1d/%s.shtml"

AURL = "http://www.weather.com.cn/air/?city=101130101"

def crawlWeather(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    return soup





if __name__ == "__main__":
    code = "101130101"
    url = AURL
    header = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
    }
    para = {"city" : code}
    cookie = {
        "weather_defaultCity":"101130101%7C%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90",
        "weather_browseCity":"101130101%7C%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90",
        "cjs":"www.zgswcn.com",
        "vjuids": "-297881b24.159c6ed0efd.0.cccb058c4242a",
        "BIGipServerwww_pool":"498664509.20480.0000",
        "the_cookie":"65",
        "__asc":"b4c55444159f580c076ab5a4d09",
        "__auc":"7e685c78159c6f8b59725322656",
        "vjlast":"1485101142.1485878992.11",
        "f_city":"%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90%7C101130101%7C"}
    body = requests.get(url, headers=header, params=para, cookies=cookie)
    body.encoding = 'utf-8'
    res = crawlWeather(body.text)
    print(res)
