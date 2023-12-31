'''用于请求网络
Version : 1.0.0.0
Date : 2023/07/29 11:14
Author : Long17369
'''
import requests


def GET():
    """用于得到key&token"""
    url = 'https://cn.bing.com/translator'
    sign = ['var', 'params_AbusePreventionHelper', '=']
    HTML = requests.get(url).text
    print(type(HTML))
    TEXT1 = HTML.split(';')
    length = len(TEXT1)
    for i in range(length):
        TEXT2 = TEXT1[i].split()
        if len(TEXT2) == 4:
            x0 = TEXT2[0] == sign[0]
            x1 = TEXT2[1] == sign[1]
            x2 = TEXT2[2] == sign[2]
            x = x0 and x1 and x2
            if x:
                TEXT3 = TEXT2[3][1:-1].split(',')
                print(TEXT3)
                break
    key = TEXT3[0]
    token = TEXT3[1]
    return key, token


if __name__ == '__main__':
    key, token = GET()
    print('key:', key, '\ntoken:', token)
