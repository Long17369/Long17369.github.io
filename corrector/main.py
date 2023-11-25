'''用于纠正单词错误
Version : 1.0.0.0
Date : 2023/11/25 10:40
Author : Long17369
'''


import json         # 用于读取json
import requests     # 用于请求网络
from translation.main import setting

class Corrector():
    """纠正者"""

    def __init__(self) -> None:
        self.setting = setting.get('key')
        self.formdata = setting.get('correctorformdata')
        self.url = setting.get('urlcorrector')
        self.header = setting.get('header')

    def corrector(self):
        ...