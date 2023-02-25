import os
import json

path = str(os.path.dirname(os.path.abspath(__file__))) + '\\'


def config_init():
    init = {'bilibili_cookie': "none", 'setup': 'no'}
    with open(path + 'fz_tool_config.json', 'w') as f:
        f.write(json.dumps(init))
        f.close()


def change_config(keys, valves):
    read = open(path + 'fz_tool_config.json', 'r+')
    data = json.loads(read.read())
    read.close()
    writes = open(path + 'fz_tool_config.json', 'w+')
    data[keys] = valves
    writes.write(json.dumps(data))
    writes.close()


def check_config():
    if 'fz_tool_config.json' not in os.listdir(path):
        config_init()
    a = open(path + 'fz_tool_config.json', 'r')
    data = a.read()
    if data == '':
        config_init()


def check_init():
    a = open(path + 'fz_tool_config.json', 'r')
    data = json.loads(a.read())
    a.close()
    if data['setup'] == 'no':
        os.system('pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple')
        change_config('setup', 'yes')


def init_():
    check_config()
    check_init()
