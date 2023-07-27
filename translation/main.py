'''用于请求翻译'''


import json         # 用于读取json
import requests     # 用于请求网络


class Translate():
    """翻译"""
    def __init__(self) -> None:
        self.token = 'NTuUIMBqLrZQ98bEVlO33MSmXU6QiN5R'
        self.key = '1690370670467'

    class Simple():
        """简单翻译"""
        def __init__(self) -> None:
            self.setting = setting.get('key')
            self.formdata = setting.get('formdata')
            self.error = setting.get('sign')["translate"]
            self.url = setting.get('url')
            self.header = setting.get('header')
            self.formdata.update(setting.get('key'))
        def reload(self,fun):
            """重载key&token"""
            self.formdata.updata(setting.get('key'))
            return fun
        def simple(self,info):
            """简单翻译"""
            self.formdata["text"] = info
            word = requests.post(self.url, data=self.formdata, headers=self.header, timeout=10).json()
            if word == self.error:
                # print('key, token已失效')
                keyToken()
                self.reload(self.simple)(info)
            return word

    class Complex():
        """复杂翻译"""
        def __init__(self) -> None:
            self.setting = setting.get('key')
            self.formdata = setting.get('formdata')
            self.error = setting.get('sign')["translate"]
            self.url = setting.get('url')
            self.header = setting.get('header')
            self.formdata.update(setting.get('key'))
        def reload(self,fun):
            """重载key&token"""
            self.formdata.updata(setting.get('key'))
            return fun
        def complex(self,info):
            """复杂翻译"""
            self.formdata["text"] = info
            word = requests.post(self.url, data=self.formdata, headers=self.header, timeout=10).json()
            if word == self.error:
                # print('key, token已失效')
                keyToken()
                self.reload(self.complex)(info)
            return word

translate = Translate()


def get_key_and_token():
    """用于得到key和token"""
    url = 'https://cn.bing.com/translator'
    sign = ('var', 'params_AbusePreventionHelper', '=',)
    html1 = requests.get(url, timeout=10).text
    print(type(html1))
    text1 = html1.split(';')
    length = len(text1)
    for i in range(length):
        text2 = text1[i].split()
        if len(text2) == 4:
            Yesnot = [text2[i] == sign[i] for i in range(2)]
            yesnot = Yesnot[0] and Yesnot[1] and Yesnot[2]
            if yesnot:
                text3 = text2[3][1:-1].split(',')
                print(text3)
                break
    key = {"key":text3[0],"token":text3[1]}
    setting.set("key",key)
keyToken = get_key_and_token

class Setting():
    """用于读写设置"""
    def __init__(self) -> None:
        self.set = self.setSetting
        self.get = self.getSetting
    def getSetting(self,settingB: str = 'setting'):
        """用于读取设置"""
        with open('./setting.json', 'r', encoding='utf-8') as f:
            settings = json.load(f)
        if settingB in settings:
            return settings[settingB]
        if settingB == 'setting':
            return settings
        print('Setting Not Found')
        return None
    def setSetting(self,settingB = None,settingC = None):
        """用于写入设置"""
        if settingB is None or settingC is None:
            return None
        settings = self.getSetting()
        settings[settingB] = settingC
        with open('./setting.json', 'w', encoding='utf-8') as f:
            json.dump(settings,f,sort_keys=True,indent=True)

setting = Setting()


if __name__ == '__main__':
    print('          翻译结果由微软翻译提供！（请确保网络已连接）')
    while True:
        trans = input('翻译内容：')
        words = translate.simple(trans)
        print(words, '\n')

