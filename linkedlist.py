#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 节点
class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

# 反转单链表
def reversed(head):
    # 设置向前指针
    # 每次遍历更改head指针和prev指针
    # 当head指针指向之前链表null时，返回prev即为head
    prev = None
    while head:
        tmp = head.next # 保存当前next指针
        head.next = prev
        prev = head
        head = tmp
    return tmp


# 反转单链表
def reverse(head):
    if not head or not head.next:
        return head
    prev = None
    while head:
        tmp = head.ne
        tmp = head.next # 缓存当前节点向后指针
        head.next = prev # 反转关键
        prev = head
        head = tmp
    return prev

# SingleLinkedList
class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # 从链表头部插入
    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp

    # 从链表尾部插入
    def append(self, item):
        tmp = Node(item)
        if self.isEmpty():
            self.head = tmp
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(tmp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        current = self.head
        count = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                count = count + 1
        if found:
            return count
        else:
            raise ValueError, "%s is not in the list" % item

    # remove方法 考虑 pre指针
    def remove(self, item):
        current = self.head
        pre = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                pre = current
                current = current.getNext()
        if pre == None:
            self.head = current.getNext()
        else:
            pre.setNext(current.getNext())

    # insert
    def insert(self, pos, item):
        if pos == self.size():
            self.append(item)
        else:
            tmp = Node(item)
            count = 1
            pre = None
            current = self.head
            while count <= pos and current != None:
                if count == pos:
                    pre = current.getNext()
                    current.setNext(tmp)
                    tmp.setNext(pre)
                else:
                    current = current.getNext()
                    count = count + 1
                    self.size = self.size + 1


if __name__ == '__main__':
    l = SingleLinkedList()
    l.add(3)
    l.add(4)
    l.append(5)
    print l.index(6)
