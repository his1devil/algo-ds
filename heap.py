#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""
通常指二叉堆，是近似完全二叉树的数据结构
常被用作实现优先队列
"""
class MaxHeap(object):
    def __init__(self, array=None):
        if array:
            self.heap = self._max_heapify(array)
        else:
            self.heap = []

    def _sink(self, array, i):
        left = i*2 + 1
        right = i*2 + 2
        max_index = i
        if left < len(array) and array[left] > array[max_index]:
            max_index = left
        if right < len(array) and array[right] > array[max_index]:
            max_index = right
        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
            self._sink(array, max_index)

    def _swim(self, array, i):
        if i == 0:
            return
        father = (i-1)/2
        if array[father] < array[i]:
            array[father], array[i] = array[i], array[father]
            self._swim(array, father)


    def _max_heapify(self, array):
        for i in xrange(len(array) / 2, -1, -1):
            self._sink(array, i)
        return array

    def push(self, item):
        self.heap.append(item)
        self.swim(self.heap, len(self.heap) - 1)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        item = self.heap.pop()
        self._sink(self.heap, 0)
        return item

HEAP_SIZE = 0
LEFT = lambda i: i*2+1
RIGHT = lambda i: i*2+2
# 保持大根堆
def heapify(alist, i):
    l, r = LEFT, RIGHT
    max_index = i
    if l < len(alist) and alist[l] > alist[max_index]:
        max_index = l
    if r < len(alist) and alist[r] > alist[max_index]:
        max_index = r
    if max_index != i:
        alist[i], alist[max_index] = alist[i], alist[max_index]
        heapify(alist, max_index)

# 创建大根堆
def build_max_heap(alist):
    for i in xrange(len(alist)//2 - 1, -1, -1):
        heapify(alist, i)

# heap sort
def heap_sort(alist):
    """
    移除根节点，并做最大堆调整递归
    """
    # 最后一个父节点, 下标从0开始
    first = len(alist) // 2 - 1
    for start in xrange(first, -1, -1):
        # 开始构造大根堆
        max_heapify(alist, start, len(alist)-1)
    for end in xrange(len(alist)-1, 0, -1): # heap sort
        alist[end], alist[0] = alist[0], alist[end]
        max_heapify(alist, 0, end-1)
    return alist


def max_heapify(array, start, end):
    """
     大根堆调整，调整子节点，总是小于父节点
    """
    root = start
    while True:
        child = root*2 + 1
        if child > end:
            break
        if child+1 <= end and array[child] < array[child+1]:
            child = child + 1
        if array[root] < array[child]: # 大的子节点成为父节点
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break
