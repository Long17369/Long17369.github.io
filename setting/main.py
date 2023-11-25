'''设置相关
Version : 1.0.0.0
Date : 2023/11/25 10:50
Author : Long17369
'''

import json         # 用于读取json
import requests     # 用于请求网络


class Setting():
    """用于读写设置"""

    def __init__(self) -> None:
        self.set = self.setSetting
        self.get = self.getSetting

    def getSetting(self, settingB: str = 'setting'):
        """用于读取设置"""
        with open('./setting/setting.json', 'r', encoding='utf-8') as f:
            settings = json.load(f)
        if settingB in settings:
            return settings[settingB]
        if settingB == 'setting':
            return settings
        print('Setting Not Found')
        return None

    def setSetting(self, settingB=None, settingC=None):
        """用于写入设置"""
        if settingB is None or settingC is None:
            return None
        settings = self.getSetting()
        settings[settingB] = settingC
        with open('./setting/setting.json', 'w', encoding='utf-8') as f:
            json.dump(settings, f, sort_keys=True,
                      indent=True, ensure_ascii=False)

def get_key_and_token():
    """用于得到key和token"""
    url = 'https://cn.bing.com/translator'
    sign = ('var', 'params_AbusePreventionHelper', '=',)
    html1 = requests.get(url, timeout=10).text
    text1 = html1.split(';')
    length = len(text1)
    for i in range(length):
        text2 = text1[i].split()
        if len(text2) == 4:
            Yesnot = [text2[i] == sign[i] for i in range(3)]
            yesnot = Yesnot[0] and Yesnot[1] and Yesnot[2]
            if yesnot:
                text3 = text2[3][1:-1].split(',')
                break
    key = {"key": text3[0], "token": text3[1][1:-1]}
    setting.set("key", key)


keyToken = get_key_and_token


setting = Setting()