#! /usr/bin/env python
# -*- coding: utf-8 -*-


def shellSort(alist):
    """
    希尔排序 diminishing increment sort，改进直接插入排序，非稳定排序算法
    把列表切割若干子列表，子列表使用直接插入
    切割过程不是相连元素，而是用增量i，或称gap
    其实直接插入可以看作是增量i=1的希尔

    shell sort大大减小了shift操作次数
    \来自维基百科
    关于步长的选择，Donald Shell建议步长选择为n/2并且对步长取半达到1，保证会被排序
    比较在希尔排序中是最主要的操作，而不是交换，选择合适步长Sedgewick (1, 5, 19, 41, 109...)比插入要快
    在小数组中比快排和堆排序还快，但是大量数据时比快速排序慢
    步长的选择直接决定了排序的复杂度
    """
    n = len(alist)
    gap = round(n/2)
    while gap > 0:
        for i in range(gap, n): # 对每一列进行插入排序，从gap到n-1
            tmp = alist[i]
            j = i
            while (j >= gap and alist[j-gap] > tmp): # 插入排序
                alist[j] = alist[j-gap]
                j = j - gap
            alist[j] = tmp
        gap = round(gap/2)
    return alist

def shellSort2(alist):
    # 选择步长
    gap = len(alist) // 2
    while gap > 0:
        for startposition in range(gap):
            gapInsertionSort(alist, startposition, gap)
        gap = gap // 2
    return alist

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position > 0 and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print shellSort2(alist)

