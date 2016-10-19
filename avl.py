#! /usr/bin/env python
# -*- coding: utf-8 -*-


import trees.binarysearchtree
"""
balanceFactor = height(leftSubTree) - height(rightSubTree)
平衡因子如果 > 0 left-heavy
elif < 0 right-heavy
balanceFactor = 0 完全平衡

带有平衡因子1, 0或-1的节点被认为是平衡的，平衡因子直接存储在每个节点中

节点的插入:
new leaf noded的平衡因子为0，因为当做leaf node插入，但是插入之后需要平衡parent节点
如何影响parent's的平衡因子取决于leaf node 是左节点还是右节点
如果新增leaf node是右节点，那么parent's平衡因子-1
如果新增leaf node是左节点，那么parent's平衡因子+1
递归up也适用

AVL作为binary search treed的子类实现
"""
class AVL(BinarySearchTree):
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalace(node.parent)
