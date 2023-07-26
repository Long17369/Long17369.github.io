'''用于请求网络'''
import requests


def GET():
    """用于得到key&token"""
    url = 'https://cn.bing.com/translator'
    sign0 = 'var'
    sign1 = 'params_AbusePreventionHelper'
    sign2 = '='
    HTML = requests.get(url).text
    print(type(HTML))
    TEXT1 = HTML.split(';')
    length = len(TEXT1)
    for i in range(length):
        TEXT2 = TEXT1[i].split()
        if len(TEXT2) == 4:
            x0 = TEXT2[0] == sign0
            x1 = TEXT2[1] == sign1
            x2 = TEXT2[2] == sign2
            x = x0 and x1 and x2
            if x:
                TEXT3 = TEXT2[3][1:-1].split(',')
                print(TEXT3)
                break
    key = TEXT3[0]
    token = TEXT3[1]
    return key , token


if __name__ == '__main__':
    key , token = GET()
    print('key:',key,'\ntoken:',token)
    
