"""生成随机列表
Version : 1.0.0.0
Date : 2023/07/29 11:14
Author : Long17369
"""
from random import random


class Mainfan():
    """主要方法"""
    def __init__(self) -> None:
        self.list = self.randomlist
        self.listInt = self.randomlistInt
    def randomlist(self,count:int = 10) -> list:
        """用于生成随机列表"""
        p = []
        for i in range (count):
            p.append(random())
        return p
    def randomlistInt(self,count:int = 10) -> list:
        """用于生成随机整数值列表"""
        p = self.randomlist(count)
        for i in range(count):
            p[i] = int(p[i]*count*10)
        return p

main = Mainfan()
    # randomlist	-> list

class RandomS():
    """作用未知，未完工"""
    def __init__(self) -> None:
        self.order=self.orderlist
    def orderlist(self,n):
        Order = main.list(n)
        return Order
    def orderlistInt(self,NumElement:int,max:int) ->list:
        """用于生成整数列表\n\nNumElement:生成个数\n\nmax:最大值\n\n"""
        Order = main.list(NumElement)
        for i in range(NumElement):
            Order[i] = int(Order[i]*max)
        return Order

randoms = RandomS()
    # orderlist		-> order