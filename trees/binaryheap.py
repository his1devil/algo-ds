#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
binary heap常用来实现优先队列
enqueue dequeue都是O(logn)
二叉堆有两个变种 最小堆和最大堆 min heap max heap;
子节点的键值或索引总是小于或是大于父节点

为了保证对数复杂度，需要使用平衡树
平衡二叉树大概就是左右nodes数量相同;

在heap的实现中，保证树的平衡通过创建一个完全二叉树;
完全二叉树即每一level都有nodes，除了leaf层，是从左往右填充
索引from 0
父节点 i 的左子节点位置 2*i
父节点 i 的右子节点位置 2*i+1
子节点 i 的父节点位置 i/2
"""

class BinaryHeap(object):
    def __init__(self):
        self.heapList = [0] # 为了integer division 计算 使用单list
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i // 2

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            minchild = self.minChild(i)
            if self.heapList[i] > self.heapList[minchild]:
                self.heapList[i], self.heapList[minchild] = self.heapList[minchild], self.heapList[i]
            i = minchild

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]: # 比较左右子节点
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        minVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return minVal

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1


