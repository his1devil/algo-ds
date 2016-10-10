#! /usr/bin/env python
# -*- coding: utf-8 -*-

def insertionSort(alist):
    """
    still O(n²)
    在低位始终维护一个sorted sublist，新增item insert into the previous sublist
    遍历过程中比较new item大小，shift righty bigger item
    shift操作大约cost swap操作的1/3，插入排序略好于冒泡和选择排序 只需要一步
    """
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue
    return alist

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print insertionSort(alist)
