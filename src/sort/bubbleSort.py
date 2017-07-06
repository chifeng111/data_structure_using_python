# coding: utf-8
def bubbleSort(alist):
    '''冒泡排序，直接对原列表排序，无返回值'''
    for passnum in range(len(alist)-1,0,-1):
        exchange = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        if not exchange:
            break


if __name__ == '__main__':
    print(bubbleSort.__doc__)
    alist = [54,26,93,17,77,31,44,55,20]
    bubbleSort(alist)
    print(alist)
    
    