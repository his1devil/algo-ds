#! /usr/bin/env python

"""
图的实现方式之一 - 邻接矩阵:
    使用二维矩阵，行，列代表vertex，cell中的value代表row v和coloumn w是否有edge相连

实现方式之二: 邻接表 Adjacency List:
    master list中维持vertices，每一个vertex obj有一个key为vertices values为weights的字典
    优势是可以很紧凑地表示稀疏图

"""
