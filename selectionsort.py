#! /usr/bin/env python
# -*- coding: utf-8 -*-

def selectionSort(alist):
    """
    选择排序改善了冒泡排序，每次遍历列表只运行一次swap操作
    记录最大值的位置，遍历过后进行交换
    """
    for slot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for i in range(1, slot+1):
            if alist[i] > alist[positionOfMax]:
                positionOfMax = i
        alist[slot], alist[positionOfMax] = alist[positionOfMax], alist[slot]

    return alist

alist = [26, 54, 93, 17, 77, 31, 44, 55, 20]
print selectionSort(alist)
