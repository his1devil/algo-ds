#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
树的遍历有三种 preorder, inorder, postorder
"""

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getRightChild())
        postorder(tree.getLeftChild(0))
        print(tree.getRootVal())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


"""
 树的遍历通常使用递归方式理解和实现
 深度优先 DFS: preorder, inorder, postorder 理解为用栈的思想遍历
 广度优先 BFS 理解为队列的思想遍历
"""
class Traversal(object):
    def __init__(self):
        self.traversal_path = list()

    def preorder(self, root):
        if root:
            self.traversal_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traversal_path.append(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traversal_path.append(root.val)


