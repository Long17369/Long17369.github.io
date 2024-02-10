'''初始化
Version : 1.0.0.0
Date : 2024/02/10 17:45
Author : Long17369
'''


import os
import json

dirtory = os.walk('.\\每日单词')
for (i, j, k) in dirtory:
    dirtory = k
dirtory.remove('404.html')
dirtory.remove('dir.json')
with open('.\\每日单词\\dir.json', 'w', encoding='utf-8') as f:
    json.dump(dirtory, f, sort_keys=True, indent=True, ensure_ascii=False)
