import requests
import json
import re

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}


def ip138(ip):
    try:
        q = requests.get('https://ip138.com/iplookup.php?ip=' + str(ip), headers=header).text
        return re.findall('<td><span>(.*?)</span></td>', q)[0]
    except:
        return 'Error.'


def ip_cn(ip):
    try:
        q = requests.get('https://ip.cn/ip/' + ip + '.html', headers=header).text
        return re.findall('<div id="tab0_address">(.*?)</div>', q)[0]
    except:
        return 'Error.'


def baidu(ip):
    try:
        q = requests.get('http://opendata.baidu.com/api.php?query=' + ip + '&co=&resource_id=6006&oe=utf8').text
        jsons = json.loads(q)
        return jsons['data'][0]['location']
    except:
        return 'Error.'


def ip_api_com(ip):
    try:
        q = json.loads(requests.get('http://ip-api.com/json/' + ip + '?lang=zh-CN').text)
        return q["country"] + '  ' + q["regionName"]
    except:
        return 'Error.'


def get_ip():
    ip = re.findall('\d+\.\d+\.\d+\.\d+', requests.get('https://www.taobao.com/help/getip.php').text)[0]
    return ip