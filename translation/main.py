'''用于请求网络'''
import requests


def translate_weiruan(info):
    """翻译"""
    token = 'NQJdw0JLe1Hn_1Wga7Ly47iLgZOdFkK1'
    key = '1690366476449'
    url1 = 'http://cn.bing.com/ttranslatev3?isVertical=1&&IG='
    url2 = '5203357EA2EF4807ADCB196ED95F24D5'
    url3 = '&IID=translator.5026'
    url=url1+url2+url3
    formdata={
        'fromLang':'en',
        'text':info,
        'to':'zh-Hans',
        'token':token,
        'key':key,
        'tryFetchingGenderDebiasedTranslations':'ture'}
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
    print(word)
    print('翻译结果：')


if __name__ == '__main__':
    print('          翻译结果由微软翻译提供！（请确保网络已连接）')
    while True:
        trans = input('翻译内容：')
        translate_weiruan(trans)
        print('\n')
