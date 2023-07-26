'''用于请求网络'''
import requests


def translate_weiruan(info):
    """翻译"""
    with open('./setting.json','r',encoding="utf-8"):
        ...
    token = 'NTuUIMBqLrZQ98bEVlO33MSmXU6QiN5R'
    key = '1690370670467'
    sign = {'statusCode': 205, 'errorMessage': ''}
    url1 = 'http://cn.bing.com/ttranslatev3?isVertical=1&&IG='
    url2 = '5203357EA2EF4807ADCB196ED95F24D5'
    url3 = '&IID=translator.5026'
    url=url1+url2+url3
    formdata={
        "fromLang":"en",
        "text":info,
        "to":"zh-Hans",
        "token":token,
        "key":key,
        "tryFetchingGenderDebiasedTranslations":"ture"}
    header = {
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.115",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://cn.bing.com",
        "sec-ch-ua-arch": "x86",
        "sec-ch-ua-bitness": "64",
        "sec-ch-ua-full-version": "109.0.1518.115",
        "sec-ch-ua-full-version-list":"Not_A Brand;v=99.0.0.0,Microsoft Edge;v=109.0.1518.115,Chromium;v=109.0.5414.149",
        "sec-ch-ua-platform": "Windows",
        "sec-ch-ua-platform-version": "0.1.0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"}
    word = requests.post(url,data=formdata,headers = header,timeout=10).json()
    if word == sign:
        print('key, token已失效')
    return word


def get_key_and_token():
    """用于得到key和token"""
    url = 'https://cn.bing.com/translator'
    sign = ('var','params_AbusePreventionHelper','=',)
    html1 = requests.get(url,timeout=10).text
    print(type(html1))
    text1 = html1.split(';')
    length = len(text1)
    for i in range(length):
        text2 = text1[i].split()
        if len(text2) == 4:
            Yesnot = (text2[i] == sign[i] for i in range(2))
            yesnot = Yesnot[0] and Yesnot[1] and Yesnot[2]
            if yesnot:
                text3 = text2[3][1:-1].split(',')
                print(text3)
                break
    key = text3[0]
    token = text3[1]
    return key , token


if __name__ == '__main__':
    print('          翻译结果由微软翻译提供！（请确保网络已连接）')
    while True:
        trans = input('翻译内容：')
        words = translate_weiruan(trans)
        print(words,'\n')
