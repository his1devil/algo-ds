#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
解析树
"""
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class BinaryTree(object):
    def __init__(self, newobj):
        self.key = newobj
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

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, newroot):
        self.key = newroot

    def getRootVal(self):
        return self.key

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError

pt = buildParseTree("((10+5)*3)")
print pt

