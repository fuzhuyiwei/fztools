import requests
import re
import os

count = 0
true_list = []
pros = {}


def get_proxy(country, type):
    if country == '':
        country = 'US'
    if type == '':
        type = 'http'
    try:
        a = requests.get('https://www.proxy-list.download/api/v1/get?type=' + type + '&country=' + country)
        proxy = re.findall('(.*?)\r\n', a.text)
        return proxy[0]
    except:
        return 'Error'


def wget_github_proxy(url, download):
    if url == '':
        print('请输入url！')
    if download == True:
        os.system('wget ' + 'https://ghproxy.com/' + url)
    else:
        return 'wget ' + 'https://ghproxy.com/' + url


def pip_proxy(package):
    return 'pip install ' + package + ' -i https://pypi.tuna.tsinghua.edu.cn/simple'


def wget_proxy(url, proxy):
    return 'wget -e http://' + proxy + ' ' + url
