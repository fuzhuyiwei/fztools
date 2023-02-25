import json
import re
import bilibili
import geoip
import proxys
import tools
import weather
import os

path = str(os.path.dirname(os.path.abspath(__file__))) + '\\'

weather_usage = '''
用法:
weather [Options]

Options:
    now -----------------------------  查看当前天气
    future [day]---------------------  查看天气预报，day表示几天后（1~6）最多可以查询6天后
    -f ------------------------------  与future相同
'''
geoip_usage = '''
用法:
geoip [ip Address]
'''
bilibili_usage = '''
用法：
bilibili [Options]
Options:
    msg:
        msg  ----------------------------  查看自己的私信以及回复等信息
        likes  --------------------------  查看点赞的相关信息
    setcookie [cookie]  -----------------  设置自己的bilibili_cookie信息

'''
usage_list = [
    ['weather', 'geoip', 'bilibili', 'piproxy', 'gitproxy', 'getproxy'],
    ['查看当前 / 未来的天气', '查询ip属地', '查看bilibili的事件', '代理pip下载', '代理github文件下载', '获取代理ip']
]
shell_command_list = [
    ['weather', 'weather ?', 'weather -?', 'weather -h', 'weather --help'],
    ['geoip', 'geoip ?', 'geoip -?', 'geoip -h', 'geoip --help'],
    ['bilibili', 'bilibili ?', 'bilibili -?', 'bilibili -h', 'bilibili --help']
]
welcome = '''
 欢迎使用FZ Tools
 作者：腐竹一位
---------------------------------------
 _____ _____  _____           _
|  ___|__  / |_   _|__   ___ | |  ___
| |_    / /    | |/ _ \ / _ \| | / __|
|  _|  / /_    | | (_) | (_) | | \__ \\
|_|   /____|   |_|\___/ \___/|_| |___/
    使用 “help” 获取命令帮助
'''
print(welcome, end='')

tools.init_()


def change_config(keys, valves):
    read = open('fz_tool_config.json', 'r+')
    data = json.loads(read.read())
    read.close()
    writes = open('fz_tool_config.json', 'w+')
    data[keys] = valves
    writes.write(json.dumps(data))
    writes.close()


def output_command_list():
    for x in range(len(usage_list[0])):
        print(usage_list[0][x] + "\t\t\t", end='')
        print(usage_list[1][x])


def set_bilibili_cookie(cookie):
    read = open(path + 'fz_tool_config.json', 'r+')
    data = json.loads(read.read())
    read.close()
    writes = open(path + 'fz_tool_config.json', 'w+')
    data['bilibili_cookie'] = cookie
    writes.write(json.dumps(data))
    writes.close()
    print('bilibili cookie修改成功！')


while True:
    shell = input('fz_tool >')
    if shell == 'weather now':
        weather.weather_info(weather.get_city())

    elif shell in shell_command_list[0]:
        print(weather_usage)

    elif len(re.findall('weather future \d', shell)) == 1 or len(re.findall('weather -f \d', shell)) == 1:
        if len(re.findall('weather future \d', shell)) == 1:
            days = re.findall('weather future (\d)', shell)[0]
        else:
            days = re.findall('weather -f (\d)', shell)[0]
        weather.future_weather_info(weather.get_city(), day=int(days))

    elif shell in shell_command_list[1]:
        print(geoip_usage)

    elif len(re.findall('geoip (\d+\.\d+\.\d+\.\d+)', shell)) == 1:
        ip = re.findall('geoip (\d+\.\d+\.\d+\.\d+)', shell)[0]
        print("    ip138.com：", end='')
        print(geoip.ip138(ip))
        print("    ip.cn：", end='')
        print(geoip.ip_cn(ip))
        print("    opendata.baidu.com：", end='')
        print(geoip.baidu(ip))
        print("    ip-api.com：", end='')
        print(geoip.ip_api_com(ip))

    elif len(re.findall('gitproxy (.*?)', shell)) == 1:
        print(proxys.wget_github_proxy(re.findall('gitproxy (.*)', shell)[0], False))

    elif len(re.findall('piproxy (.*?)', shell)) == 1:
        print(proxys.pip_proxy(re.findall('piproxy (.*)', shell)[0]))

    elif len(re.findall('getproxy', shell)) == 1:
        print(proxys.get_proxy('', ''))

    elif shell == 'getip':
        print('您的ip地址是：', end='')
        print(geoip.get_ip())

    elif shell == 'bilibili msg':
        bilibili.massages()

    elif len(re.findall('bilibili setcookie (.*?)', shell)) == 1:
        set_bilibili_cookie(re.findall('bilibili setcookie (.*)', shell)[0])

    elif len(re.findall('bilibili msg likes (\d*)', shell)) == 1:
        bilibili.likes(int(re.findall('bilibili msg likes (\d*)', shell)[0]))

    elif len(re.findall('bv2av (.*)', shell)) == 1:
        if len(re.findall('bv2av (BV([a-z]|[A-Z]|[0-9]*){12})', shell)) == 1:
            print(bilibili.bv_to_av(re.findall('bv2av (.*)', shell)[0]))
        else:
            print('请输入正确的bv号！')

    elif len(re.findall('av2bv (.*)', shell)) == 1:
        if len(re.findall('av2bv (av[0-9]*)', shell)) == 1:
            print(bilibili.av_to_bv(re.findall('av2bv (.*)', shell)[0]))
        else:
            print('请输入正确的av号！')

    elif shell == 'weather future':
        print('weather： 请补全数值：[day]')

    elif shell == 'help':
        print('输入 [command] --help 获取命令的详细信息。')
        output_command_list()

    elif shell in shell_command_list[2]:
        print(bilibili_usage)

    elif shell == "!!quit" or shell == "!q":
        quit()

    else:
        if shell != '':
            print(shell + '：  没有这个命令!')
