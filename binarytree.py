#! /usr/bin/env python
# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Traversal(object):
    """
    深度优先利用栈(递归)的思想遍历树，广度优先利用队列思想
    """
    def __init__(self):
        self.traversa_path = list()

    def preorder(self, root):
        if root:
            self.traversa_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traversa_path.append(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traversa_path.append(root.val)
