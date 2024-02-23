'''目录(已废弃)
Version : 1.0.0.0
Date : 2024/02/10 17:45
Author : Long17369
'''

import os

class Dirtory():
    def __init__(self) -> None:
        self.getDirName = self.getDirtoryName
        pass
    
    def getDirtoryName(self, dir):
        w = os.walk(dir)
        return w



dirtory = Dirtory()

if __name__ == '__main__':
    for (dirpath,dirname,filenames) in dirtory.getDirName('.\\'):
        print (filenames)