# coding: utf-8
def selectionSort(alist):
    '''选择排序，每次选择最大的放在无序列表的最后'''
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
    
        alist[fillslot], alist[positionOfMax] = \
        alist[positionOfMax], alist[fillslot]


if __name__ == '__main__':
    print(selectionSort.__doc__)
    alist = [54,26,93,17,77,31,44,55,20]
    selectionSort(alist)
    print(alist)
    
    
    