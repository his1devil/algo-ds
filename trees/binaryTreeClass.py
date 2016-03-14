#! /usr/bin/env python
# -*- coding: utf-8 -*-

# OO 构造二叉树
class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

r = BinaryTree('a')
print r.getRootVal() # a
print r.getLeftChild() # None

r.insertLeft('b')
print r.getLeftChild() # <__main__.BinaryTree object at 0x1075b3c50>
print r.getLeftChild().getRootVal() # b

r.insertRight('c')
print r.getRightChild() # <__main__.BinaryTree object at 0x104430c90>
print r.getRightChild().getRootVal() # c

r.getRightChild().setRootVal('hello')
print r.getRightChild().getRootVal() # hello


