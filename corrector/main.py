'''用于纠正单词错误
Version : 1.0.0.0
Date : 2023/11/25 10:40
Author : Long17369
'''


import json         # 用于读取json
import requests     # 用于请求网络
from setting.main import setting,keyToken


class Corrector():
    """纠正者"""

    def __init__(self) -> None:
        self.formdata = setting.get('correctorformdata')
        self.url = setting.get('urlcorrector')
        self.header = setting.get('header')
        self.formdata.update(setting.get('key'))
        self.cor = self.corrector

    def reload(self,fun):
        """重载key&token"""
        self.formdata.update(setting.get('key'))
        return fun

    def corrector(self, info):
        """纠正单词"""
        words = {}
        with open('./word/word.json', 'r', encoding='utf-8') as f:
            words = json.load(f)
        word = [j for i in words for j in i['word']]
        error = {}
        percent = 0
        for i in range(len(word)):
            if ((i+1)/len(word))*100-percent > 0.1:
                print('进度：',str(percent)+'%')
                percent = ((i+1)/len(word))*100
            self.formdata["text"] = word[i]
            post = requests.post(self.url, data=self.formdata,
                                 headers=self.header, timeout=10)
            info = post.json()['correctedText']
            if info == '':
                # print(word[i])
                ...
            else:
                # print(word[i],info)
                error.update({i:word[i]})
        return error


corrector = Corrector()
cor = corrector.cor
