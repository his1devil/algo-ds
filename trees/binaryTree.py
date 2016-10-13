#! /usr/bin/env python
# -*- coding: utf-8 -*-


class BinaryTree(object):
    """
    OOP
    """
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newnode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newnode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.rightChild = self.rightChild
            self.rightChild = t

    """
     访问器方法
    """
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, newobj):
        self.key = newobj

    def getRootVal(self):
        return self.key
