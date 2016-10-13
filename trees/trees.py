#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Tree(object):
    """
    if each node in the tree has a maximum of 2 children - binary tree
    tree的表示
    myTree = ['a', # root
            ['b', # left subtree
            ['d', [], []],
            ['e', [], []] ],

            ['c', # right subtree
            ['f', [], []],
            [] ]
            ]
    """
    def binaryTree(r):
        return [r, [], []]

    def insertLeft(root, newbranch):
        t = root.pop(1)
        if len(t) > 1:
            root.insert(1, [newbranch, t, []])
        else:
            root.insert(1, [newbranch, [], []])

    def insertRight(root, newbranch):
        t = root.pop(2)
        if len(t) > 1:
            root.insert(2, [newbranch, [], t])
        else:
            root.insert(2, [newbranch, [], []])

    def getRootVal(root):
        return root[0]

    def setRootVal(root, newVal):
        root[0] = newVal

    def gerRightChild(root):
        return root[2]
