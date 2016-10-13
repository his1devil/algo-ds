#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
# 快排首先要选择一个pivot value用来调校list splited (这里选第一个)
# pivot value最终所处位置称为split point，用来分割子列表
# 快排的关键在于partition function
# 首先partitioning标记两个位置 leftmark和rightmark(pivot value外列表的左端和右端)
# 遍历增加leftmark，直到找到> pivot value的值的位置，然后遍历递减rightmark，直到找到 < pivot value的位置
# when rightmark < leftmark, stop, rightmark即为split point
# 然后对splited list各自递归quick sort

复杂度分析: 对于长度为n的list，如果partition总是出现在middle处，将会产生logn次divisions，为了找到split point
每一个item都需要进行和pivot value对比，即nlogn，而且在merge阶段不需要额外的存储空间

不过，最坏的情况是split points不在middle位，靠近左端或是右端，造成非常不均衡的division，结果可能就是O(n²)

选择pivot value的方法不止一种，这里使用median of three方法减少uneven division:
    首先考虑list中first, middle和last的值，实例54, 77, 20
    选择median value，即54作为pivot value

'''

def quickSort(L):
    quickSortHelper(L, 0, len(L) - 1)

def quickSortHelper(L, first, last):
    splitpoint = partition(L, first, last)
    quickSortHelper(L, first, splitpoint - 1)
    quickSortHelper(L, splitpoint + 1, last)

def partition(L, first, last):
    pivotvalue = L[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and L[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while leftmark <= rightmark and L[rightmark] >= pivotvalue:
            rightmark = rightmark - 1
        if rightmark <= leftmark:
            done = True
        else:
            tmp = L[leftmark]
            L[leftmark] = L[rightmark]
            L[rightmark] = tmp
    tmp = L[first]
    L[first] = L[rightmark]
    L[rightmark] = tmp

    return rightmark


def quick_sort(alist):
    """
    quick sort通常比同为O(nlogn)的其他算法更快
    分治思想 和归并不同，并没有使用额外的存储空间
    """
    return quicksort(alist, 0, len(alist)-1)

def quicksort(alist, left, right):
    """
    bubble sort, selection sort, insertion sort O(n²)复杂度
    shell sort 不稳定 O(n) ~ O(n²)
    merge sort O(nlogn)，但是需要额外的存储空间
    quick sort O(nlogn)，不需要额外存储空间，但是如果pivot value选的不好，有可能O(n²):
    """
    if left >= right:
        return alist
    pivot = alist[left]
    i = left
    j = right
    while i < j:
        while alist[j] >= pivot and i < j:
            j -= 1
        while alist[i] <= pivot and i < j:
            i += 1
        alist[i], alist[j] = alist[j], alist[i]
    alist[left], alist[i] = alist[i], alist[left]
    quicksort(alist, left, i-1)
    quicksort(alist, j+1, right)
    return alist

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print quick_sort(alist)

