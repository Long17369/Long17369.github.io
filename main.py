"""单词处理
Version : 1.0.0.0
Date : 2023/07/29 11:14
Author : Long17369
"""
import glob
import json  # 读取json
from translation.main import translate  # 翻译
from pythonKu.randomtuple import randoms
from pythonKu.sort import bubble as sort


def synonym(file):
    """批量翻译"""
    with open(file, 'r', encoding='utf-8') as f:
        words = json.load(f)
        for i in words['word']:
            translate.complex(i)


def new_word(file,name):
    word = []
    with open(file, 'r', encoding='utf-8') as f:
        words = f.read().split('\n')
    for i in words:
        if i == []:
            pass
        else:
            duanyu = False
            wordi = {'name':'','word':[]}
            Temp = i.split('(')
            Temp[0]=')'+Temp[0]
            Word = []
            for j in Temp:
                Temp2 = j.split(')')
                Word.append(Temp2[0])
                try:
                    Word.extend(Temp2[1].split())
                except IndexError:
                    ...
            while '' in Word:
                Word.remove('')
            wordi['name']=Word[-1]
            del Word[-1]
            wordi['word'] = Word
            word.append(wordi)
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(word, f, sort_keys=True,
                          indent=True, ensure_ascii=False)


def allword(file , Name,trans:bool =False):
    """导入单词表"""
    with open(file, 'r', encoding='utf-8') as f:
        words = json.load(f)
        for i in words:
            Words = i['word']
            if trans:
                for j in Words:
                    write(j, i['name'],Name)
                    translate.complex(j)
            else:
                for j in Words:
                    write(j, i['name'],Name)


def write(word, name, Name):
    """写入单词"""
    file = './word/'+Name+'/' + word + '.json'
    ttry = True
    try:
        f = open(file, 'r', encoding='utf-8')
        f.close()
    except FileNotFoundError:
        ttry = False
        info = {"word": word, "name": []}
    if ttry:
        with open(file, 'r', encoding='utf-8') as f:
            info = json.load(f)
    with open(file, 'w', encoding='utf-8') as f:
        info["name"].append(name)
        json.dump(info, f, sort_keys=True, indent=True, ensure_ascii=False)


def split(files=''):
    """拆分每日单词"""
    if files == '':
        files = glob.glob('./每日单词/7.*.json')
    else:
        files = ['./每日单词/' + files + '.json']
    word = set()
    for i in files:
        with open(i, 'r', encoding='utf-8') as f:
            words = json.load(f)
            for i in words['word']:
                word.add(i)
    for i in word:
        fp = './word/all/'+i + '.json'
        try:
            with open(fp, 'r', encoding='utf-8'):
                ...
        except FileNotFoundError:
            file = {"name": [], "word": i}
            with open(fp, 'w', encoding='utf-8') as f:
                json.dump(file, f, sort_keys=True,
                          indent=True, ensure_ascii=False)


def read():
    """读取所有单词"""
    file = glob.glob('./word/all/*.json')
    word = []
    for i in file:
        word.append(i[11:-5])
    with open('words.txt', 'w', encoding='utf-8') as f:
        for i in word:
            f.write(i)
            f.write('\n')


def selection(date):
    with open('./words.txt', 'r', encoding='utf-8') as f:
        words = f.read().split('\n')
    List = sort(randoms.orderlistInt(10, len(words)))
    word = []
    for i in List:
        word.append(words[i])
    n = 0
    for i in List:
        words.pop(i-n)
        n += 1
    with open('./words.txt', 'w', encoding='utf-8') as f:
        for i in words[0:-1]:
            f.write(i+'\n')
        f.write(words[-1])
    del words
    words = {"word": word, "Version": {"time": date}}
    file = './每日单词/' + date + '.json'
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(words, f, sort_keys=True, indent=True, ensure_ascii=False)


if __name__ == '__main__':
    # day = './每日单词/'+input('请输入日期')+'.json'
    # synonym(day)
    # allword('word2.json','all2',True)
    # read()
    # selection(date=input("请输入日期"))
    new_word('words/word2.txt','word3.json')