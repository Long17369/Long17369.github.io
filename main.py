"""翻译"""
import json #读取json
from translation.main import translate #翻译


def tran(file):
    """批量翻译"""
    with open(file,'r',encoding='utf-8') as f:
        words = json.load(f)
        for i in words['words']:
            translate.complex(i)

if __name__ == '__main__':
    day = input('请输入日期')
    tran(day)