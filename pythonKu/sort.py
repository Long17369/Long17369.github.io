# 排序算法
# 已完成：
    # 冒泡排序		bubble
    # 快速排序		quick
    # 计数排序		count

class Bubble_sort(): # 冒泡排序
    def __init__(self) -> None:
        self.List = self.bubbleList

    def bubbleList(self,List:list):
        n = len(List)
        for i in range(1,n):
            for j in range(0,n-i):
                if List[j] > List[j+1]:
                    List[j], List[j+1] = List[j+1], List[j]
        return List

Bubble = Bubble_sort()
bubble = Bubble.List
# bubbleList		-> List 冒泡排序(列表)
# 
# 完成


class CocktailShaker_sort(): # 鸡尾酒排序(双向冒泡)
    def __init__(self) -> None:
        self.List = self.cocktailList
        pass

    def cocktailList(self,List:list):
        n = len(List)

Cocktail = CocktailShaker_sort()
cocktail = Cocktail.List
# cocktailList		-> List 鸡尾酒排序(列表)
# 
# 未完成


class Gnome_sort(): # 地精排序
    def __init__(self) -> None:
        self.List = self.gnomeList
        pass

    def gnomeList(self,List):
        n=len(List)

Gnome = Gnome_sort()
gnome = Gnome.List
# gnomeList			-> List 地精排序(列表)
# 
# 未完成


class OptimizedGnome_sort(): # 优化地精排序
    def __init__(self) -> None:
        self.List = self.optgnomeList
        pass

    def optgnomeList(self,List):
        n=len(List)

OptGnome = OptimizedGnome_sort()
optgnome = OptGnome.List
# optignomeList		-> List 优化地精排序(列表)
# 
# 未完成


class OddEven_sort(): # 奇偶排序
    def __init__(self) -> None:
        self.List = self.oddList
        pass

    def oddList(self,List):
        n=len(List)

Odd = OddEven_sort()
odd = Odd.List
# oddList			-> List 奇偶排序(列表)
# 
# 未完成


class Selection_sort(): # 选择排序
    def __init__(self) -> None:
        self.List = self.selectList
        pass

    def selectList(self,List):
        n=len(List)

Select = Selection_sort()
select = Select.List
# selectList		-> List 选择排序(列表)
# 
# 未完成


class DoubleSelection_sort(): # 双向选择排序
    def __init__(self) -> None:
        self.List = self.dselectList
        pass

    def dselectList(self,List):
        n=len(List)

DSelect = DoubleSelection_sort()
dselect = DSelect.List
# dselectList		-> List 双向选择排序(列表)
# 
# 未完成


class Insertion_sort(): # 插入排序
    def __init__(self) -> None:
        self.List = self.insertList
        pass

    def insertList(self,List):
        n=len(List)

Insert = Insertion_sort()
insert = Insert.List
# insertList		-> List 插入排序(列表)
# 
# 未完成


class BinaryInsertion_sort(): # 插入排序
    def __init__(self) -> None:
        self.List = self.bininsertList
        pass

    def bininsertList(self,List):
        n=len(List)

BinInsert = BinaryInsertion_sort()
bininsert = BinInsert.List
# insertList		-> List 插入排序(列表)
# 
# 未完成


class Comb_sort(): # 梳排序
    def __init__(self) -> None:
        self.List = self.combList
        pass

    def combList(self,List):
        n=len(List)

Comb = Comb_sort()
comb = Comb.List
# combList		-> List 梳排序(列表)
# 
# 未完成


class Shell_sort(): # 希尔排序
    def __init__(self) -> None:
        self.List = self.shellList
        pass

    def shellList(self,List):
        n=len(List)

Shell = Shell_sort()
shell = Shell.List
# shellList		-> List 希尔排序(列表)
# 
# 未完成


class Merge_sort(): # 归并排序
    def __init__(self) -> None:
        self.List = self.mergeList
        pass

    def mergeList(self,List):
        n=len(List)

Merge = Merge_sort()
merge = Merge.List
# mergeList		-> List 归并排序(列表)
# 
# 未完成

class Tim_sort(): # Tim排序
    def __init__(self) -> None:
        self.List = self.timList
        pass

    def timList(self,List):
        n=len(List)

Tim = Tim_sort()
tim = Tim.List
# timList		-> List Tim排序(列表)
# 
# 未完成

class Wiki_sort(): # 块排序
    def __init__(self) -> None:
        self.List = self.wikiList
        pass

    def wikiList(self,List):
        n=len(List)

Wiki = Wiki_sort()
wiki = Wiki.List
# wikiList		-> List 块排序(列表)
# 
# 未完成


class Quick_sort(): # 快速排序
    def __init__(self) -> None:
        self.List = self.quickList
        pass

    def quickList(self,List:list):
        n = len(List)
        self.w(List, 0, n-1)

    def w(self,List:list,start:int,end:int):
        if start >= end :
            return List
        mid = List[start]
        low = start
        high = end
        while low < high:
            while low < high and List[high] >= mid:
                high -= 1
            List[low] = List[high]
            while low < high and List[low] < mid:
                low += 1
            List[high] = List[low]
        List[low] = mid
        self.w(List, start, low-1)
        self.w(List, low + 1, end)


Quick = Quick_sort()
quick = Quick.List
# quickList		-> List 快速排序(列表)
# 
# 完成


class MaxHeap_sort(): # 最大堆排序
    def __init__(self) -> None:
        self.List = self.maxList
        pass

    def maxList(self,List):
        n=len(List)

Max = MaxHeap_sort()
max = Max.List
# maxList		-> List 最大堆排序(列表)
# 
# 未完成

class MinHeap_sort(): # 最小堆排序
    def __init__(self) -> None:
        self.List = self.minList
        pass

    def minList(self,List):
        n=len(List)

Min = MinHeap_sort()
min = Min.List
# minList		-> List 最小堆排序(列表)
# 
# 未完成

class Smooth_sort(): # 平滑排序
    def __init__(self) -> None:
        self.List = self.smoothList
        pass

    def smoothList(self,List):
        n=len(List)

Smooth = Smooth_sort()
smooth = Smooth.List
# smoothList		-> List 平滑排序(列表)
# 
# 未完成


class Tourn_sort(): # 锦标赛排序
    def __init__(self) -> None:
        self.List = self.tournList
        pass

    def tournList(self,List):
        n=len(List)

Tourn = Tourn_sort()
tourn = Tourn.List
# tournList		-> List 锦标赛排序(列表)
# 
# 未完成


class Cycle_sort(): # 循环排序
    def __init__(self) -> None:
        self.List = self.cycleList
        pass

    def cycleList(self,List):
        n=len(List)

Cycle = Cycle_sort()
cycle = Cycle.List
# cycleList		-> List 循环排序(列表)
# 
# 未完成


class Introsort(): # Intro排序
    def __init__(self) -> None:
        self.List = self.introList
        pass

    def introList(self,List):
        n=len(List)

Intro = Introsort()
intro = Intro.List
# introList		-> List Intro排序(列表)
# 
# 未完成


class Patience_sort(): # Patience排序
    def __init__(self) -> None:
        self.List = self.patienceList
        pass

    def patienceList(self,List):
        n=len(List)

Patience = Patience_sort()
patience = Patience.List
# patienceList		-> List Patience排序(列表)
# 
# 未完成


class Gravity_sort(): # Gravity排序
    def __init__(self) -> None:
        self.List = self.gravityList
        pass

    def gravityList(self,List):
        n=len(List)

Gravity = Gravity_sort()
gravity = Gravity.List
# gravityList		-> List Gravity排序(列表)
# 
# 未完成


class Count_sort(): # 计数排序
    def __init__(self) -> None:
        self.List = self.countList
        pass

    def countList(self,List):
        max=min=0
        for i in List:
            if i < min:
                min = i
            if i > max:
                max = i 
        count = [0] * (max - min +1)
        for j in range(max-min+1):
            count[j]=0
        for index in List:
            count[index-min]+=1
        index=0
        for a in range(max-min+1):
            for c in range(count[a]):
                List[index]=a+min
                index+=1

Count = Count_sort()
count = Count.List
# countList		-> List 计数排序(列表)
# 
# 完成


class Pigeonhole_sort(): # Pigeonhole排序
    def __init__(self) -> None:
        self.List = self.pigeonholeList
        pass

    def pigeonholeList(self,List):
        n=len(List)

Pigeonhole = Pigeonhole_sort()
pigeonhole = Pigeonhole.List
# pigeonholeList		-> List Pigeonhole排序(列表)
# 
# 未完成


class RadixLSD_sort(): # RadixLSD排序
    def __init__(self) -> None:
        self.List = self.radixList
        pass

    def radixList(self,List):
        n=len(List)

RadixLSD = RadixLSD_sort()
radix = RadixLSD.List
# radixList		-> List RadixLSD排序(列表)
# 
# 未完成


class AmericanFlag_sort(): # AmericanFlag排序
    def __init__(self) -> None:
        self.List = self.americanList
        pass

    def americanList(self,List):
        n=len(List)

AmericanFlag = AmericanFlag_sort()
american = AmericanFlag.List
# americanList		-> List AmericanFlag排序(列表)
# 
# 未完成


class Shatter_sort(): # Shatter排序
    def __init__(self) -> None:
        self.List = self.shatterList
        pass

    def shatterList(self,List):
        n=len(List)

Shatter = Shatter_sort()
shatter = Shatter.List
# shatterList		-> List Shatter排序(列表)
# 
# 未完成


class Flash_sort(): # Flash排序
    def __init__(self) -> None:
        self.List = self.flashList
        pass

    def flashList(self,List):
        n=len(List)

Flash = Flash_sort()
flash = Flash.List
# flashList		-> List Flash排序(列表)
# 
# 未完成


class Name_sort(): # Name排序
    def __init__(self) -> None:
        self.List = self.nameList
        pass

    def nameList(self,List):
        n=len(List)

Name = Name_sort()
name = Name.List
# nameList		-> List Name排序(列表)
# 
# 未完成


if __name__ == '__main__':
    print('代码由 Long17369、少ら龙缘 等人 编写')
    print('感谢使用该代码')