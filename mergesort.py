#! /usr/bin/env python
# -*- coding: utf-8 -*-


def merge_sort(alist):
    if len(alist) < 2:
        return alist[:]
    middle = len(alist) / 2
    left = merge_sort(alist[:middle])
    right = merge_sort(alist[middle:])
    return merged(left, right)

def merged(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def mergeSort(alist):
    """
    分治思想
    归并排序先递归分解列表，再合并
    """
    if len(alist) <= 1:
        return alist
    num = len(alist) // 2
    left = mergeSort(alist[:num])
    right = mergeSort(alist[num:])
    return merge(left, right)

def merge(left, right):
    """
    合并操作
    """
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print merge_sort(alist)
