"""单词处理"""
import glob
import json #读取json
from translation.main import translate #翻译


def synonym(file):
    """批量翻译"""
    with open(file,'r',encoding='utf-8') as f:
        words = json.load(f)
        for i in words['word']:
            translate.complex(i)

def allword(file):
    """导入单词表"""
    with open(file,'r',encoding='utf-8') as f:
        words = json.load(f)
        for i in words:
            Words = i['word']
            for j in Words:
                write(j,i['name'])

def write(word,name):
    """写入单词"""
    file = './word/all/' + word + '.json'
    ttry = True
    try:
        f = open(file,'r',encoding='utf-8')
        f.close()
    except FileNotFoundError:
        ttry = False
        info = {"word":word,"name":[]}
    if ttry:
        with open(file,'r',encoding='utf-8') as f:
            info = json.load(f)
    with open(file,'w',encoding='utf-8') as f:
        info["name"].append(name)
        json.dump(info,f,sort_keys=True,indent=True,ensure_ascii=False)

def read():
    """读取所有单词"""
    file = glob.glob('./word/all/*.json')
    word = []
    for i in file:
        word.append(i[11:-5])
    with open('words.txt','w',encoding='utf-8') as f:
        for i in word:
            f.write(i)
            f.write('\n')

if __name__ == '__main__':
    # day = './每日单词/'+input('请输入日期')+'.json'
    # allword('word.json')
    read()