'''用于请求翻译'''


import json         # 用于读取json
import requests     # 用于请求网络


def translate(info):
    """翻译"""
    token = 'NTuUIMBqLrZQ98bEVlO33MSmXU6QiN5R'
    key = '1690370670467'
    sign = "{'statusCode': 205, 'errorMessage': ''}"
    url1 = getSetting('url1')
    url2 = '5203357EA2EF4807ADCB196ED95F24D5'
    url3 = getSetting('url3')
    url = url1+url2+url3
    formdata = {
        "fromLang": "en",
        "text": info,
        "to": "zh-Hans",
        "token": token,
        "key": key,
        "tryFetchingGenderDebiasedTranslations": "ture"}
    header = getSetting('header')
    word = requests.post(url, data=formdata, headers=header, timeout=10).json()
    if word == sign:
        print('key, token已失效')
    return word


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
    key = text3[0]
    token = text3[1]
    return key, token


def getSetting(setting: str = 'setting') -> dict:
    """用于获取设置"""
    with open('./setting.json', 'r', encoding='utf-8') as f:
        settings = json.load(f)
    if setting in settings:
        return settings[setting]
    if setting == 'setting':
        return settings
    print('Setting Not Found')
    return None


if __name__ == '__main__':
    print('          翻译结果由微软翻译提供！（请确保网络已连接）')
    while True:
        trans = input('翻译内容：')
        words = translate(trans)
        print(words, '\n')
