#! /usr/bin/env python
# -*- coding: utf-8 -*-

def bubbleSort(alist):
    """
    递减最外层循环
    根据求和公式 n²/2 + n/2.... n²/2 + n/2 - n
    O(n²)比较
    """
    for passnu in range(len(alist)-1, 0, -1):
        for i in range(passnu):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

    return alist

def bubbleSortUpgrade(alist):
    """
    交换操作very costly
    在遍历中如果没有swap操作，说明已经sorted了，即可停止
    """
    swap = True
    passnu = len(alist) - 1
    while passnu > 0 and swap:
        swap = False
        for i in range(passnu):
            if alist[i] > alist[i+1]:
                swap = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnu -= 1

    return alist

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print bubbleSortUpgrade(alist)
