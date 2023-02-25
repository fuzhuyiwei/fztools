import requests
import json
import os
import tools

path = str(os.path.dirname(os.path.abspath(__file__))) + '\\'

tools.init_()


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


def decode_json(r):
    try:
        response = r.json()
    except json.JSONDecodeError:
        return -1
    else:
        return response


try:
    cookie = json.loads(open(path + 'fz_tool_config.json', 'r').read())['bilibili_cookie']
except KeyError:
    while True:
        eorro = input("cookie或config文件错误！，请尝试删除‘fz_tool_config.json’重试！\n删除吗？  y / n：")
        if eorro == 'y':
            os.remove('./fz_tool_config.json')
            quit()
        elif eorro == 'n':
            quit()
        else:
            pass
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    'cookie': cookie
}


def massages():
    q = requests.get('https://api.bilibili.com/x/msgfeed/unread', headers=head).text
    data = {}
    try:
        data = json.loads(q)['data']
    except KeyError:
        print('cookie错误,请检查cookie! ')
    try:
        print('回复我的：' + str(data['reply']) + '个')
        print('@我的：' + str(data['at']) + '个')
        print('收到的赞：' + str(data['like']) + '个')
        print('系统消息：' + str(data['sys_msg']) + '个')
        print('私信：' + str(data['chat']) + '个')
        return data['reply'], data['at'], data['like'], data['sys_msg'], data['chat']
    except:
        print("Error!")


def likes(count):
    counts = 1
    q = requests.get("https://api.bilibili.com/x/msgfeed/like", headers=head)
    data = json.loads(q.text)
    for x in data['data']['total']['items']:
        print('弹幕 / 评论：\n' + x['item']['title'])
        print('赞的类型：' + x['item']['business'])
        # print('赞的用户数量：' + str(len(x['users'])))
        for y in x['users']:
            print(y["nickname"], end="")
            if y['follow'] == True:
                print('（粉丝）', end=' ')
            else:
                print('', end=' ')
        if len(x['users']) > 5:
            print('等人赞了。', end=' ')
            break
        if len(x['users']) <= 5:
            print('赞了', end=' ')
        print("\n" + '=================' + '\n')
        if counts == count:
            break
        counts += 1


def bv_to_av(bv):
    r = requests.get('https://api.bilibili.com/x/web-interface/view', {'bvid': bv}, headers=head)
    response = decode_json(r)
    try:
        return 'av' + str(response['data']['aid'])
    except:
        return '获取av号失败'


def av_to_bv(av):
    if 'av'.lower() in av.lower():
        av = av.lower().strip('av')

    r = requests.get('https://api.bilibili.com/x/web-interface/archive/stat', {'aid': av}, headers=head)
    response = decode_json(r)
    try:
        return 'BV' + str(response['data']['bvid'])
    except (KeyError, TypeError):
        return '获取BV号失败'

if __name__ == '__main__':
    print("Here is a modle, please open 'fztool.py'to use 'bilibili.py'.")
