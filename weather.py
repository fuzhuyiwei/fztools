import requests
import json
import re

'''
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
ip = re.findall('\d+\.\d+\.\d+\.\d+', requests.get('https://www.taobao.com/help/getip.php').text)[0]


city_ = json.loads(re.sub('json:', '', requests.get('https://v.api.aa1.cn/api/api-sqdw/go.php?ip=' + ip).text))['meta']['Location.Search']["address"]
city = re.findall('(.{2})市',city_)[0]

q = requests.get(
    "https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=" + city,
    headers=header)
web = q.text
data = json.loads(web)
# dict_keys(['cityid', 'city', 'cityEn', 'country', 'countryEn', 'update_time', 'data', 'nums'])
day_data = data['data'][0]
print(data['data'][0])
print("\n====================================================\n\n")
print('更新时间：' + data["update_time"])
print("天气：" + data['data'][0]["wea"])
print('日出：' + day_data['sunrise'] + '   日落：' + day_data['sunset'])
print('风：' + day_data['win'][0] + day_data['win_speed'])
print("湿度：" + day_data['humidity'])
print("最高温度：" + re.findall("\d+ºC", day_data['narrative'])[0])

# 预警信息的清洗
if day_data['alarm'] == []:
    print("预警：无")
elif len(day_data['alarm']) > 1:
    if day_data['alarm'][len(day_data['alarm']) - 1]['alarm_type'] == day_data['alarm'][0]['alarm_type']:
        print("预警：" + day_data['alarm'][0]['alarm_type'] + day_data['alarm'][0]['alarm_level'] + "预警：")
        print(day_data['alarm'][0]['alarm_content'])
    else:
        for x in day_data['alarm']:
            print("预警：" + x['alarm_type'] + x['alarm_level'] + "预警：")
            print(x['alarm_content'])
'''
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}


def get_city():
    ip = re.findall('\d+\.\d+\.\d+\.\d+', requests.get('https://www.taobao.com/help/getip.php').text)[0]
    #http://ip-api.com/json/117.136.12.79?lang=zh-CN
    city_ = \
        json.loads(re.sub('json:', '', requests.get('https://v.api.aa1.cn/api/api-sqdw/go.php?ip=' + ip).text))['meta'][
            'Location.Search']["address"]
    city = re.findall('省(.*?)市', city_)[0]
    return city


def weather_info(city):
    q = requests.get(
        "https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=" + city,
        headers=header)
    web = q.text
    data = json.loads(web)
    day_data = data['data'][0]
    print('更新时间：' + data["update_time"])
    print("天气：" + '白天' + data['data'][0]["wea_day"] + '   晚上' + day_data['wea_night'])
    print('日出：' + day_data['sunrise'] + '   日落：' + day_data['sunset'])
    print('风：' + day_data['win'][0] + day_data['win_speed'])
    print("湿度：" + day_data['humidity'])
    print("最高温度：" + re.findall("\d+ºC", day_data['narrative'])[0])

    # 预警信息的清洗
    if day_data['alarm'] == []:
        print("预警：无")
    elif len(day_data['alarm']) > 1:
        if day_data['alarm'][len(day_data['alarm']) - 1]['alarm_type'] == day_data['alarm'][0]['alarm_type']:
            print("预警：" + day_data['alarm'][0]['alarm_type'] + day_data['alarm'][0]['alarm_level'] + "预警：")
            print(day_data['alarm'][0]['alarm_content'])
        else:
            for x in day_data['alarm']:
                print("预警：" + x['alarm_type'] + x['alarm_level'] + "预警：")
                print(x['alarm_content'])


# weather_info(get_city())


def future_weather_info(city, day):
    q = requests.get(
        'https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=' + city,
        headers=header
    ).text
    data = json.loads(q)
    # 1-6日，天气预报，6天
    day_data = data['data'][day]
    print('更新时间：' + data["update_time"])
    print('时间：' + day_data['day'])
    print("天气：" + '白天' + day_data["wea_day"] + '    晚上' + day_data['wea_night'])
    print('日出：' + day_data['sunrise'] + '   日落：' + day_data['sunset'])
    print('风：' + day_data['win'][0] + day_data['win_speed'])
    print("湿度：" + day_data['humidity'])
    print("最高温度：" + re.findall("\d+ºC", day_data['narrative'])[0])
