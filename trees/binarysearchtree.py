#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
二叉搜索树 左子节点 < parent < 右子节点
"""

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    """
    put方法 检查tree是否有root，否则create new TreeNode然后设为root
    有则call 私有递归方法_put 去搜索树，根据大小判断左右
    """
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    #
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    # 实现in 方法(contains)
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    # 删除方法
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove) # 定义remove方法
                self.size = self.size - 1
            else:
                raise KeyError('没有找到')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('没有找到')

    def __delitem__(self, key):
        self.delete(key)

    """
     remove一个nodes时需要考虑
     1. node 没有子节点
     2. node 有一个子节点
     3. node 有两个子节点
    """
    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        # 有两个子节点
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor() # 找到后继
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

    def findSuccessor(self):
        """
        考虑三种情况
        1) 如果node有一个右子树，那么succ就是这个右子树上的最小的key
        2) 如果node没有右子树并且本身是一个左子节点，那么node.parent则是successor
        3) 如果node是父节点的右子节点并且本身没有右子节点，那么node.parent则是successor
        """
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChid = self
        return succ

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


    def findMin(self):
        """
        所有二叉搜索树的最小值总是最左边的子节点
        递归each node直到node没有左子节点
        """
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

class TreeNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLefChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self




