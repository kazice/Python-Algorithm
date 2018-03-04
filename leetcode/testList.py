#!/usr/bin/python
# -*- coding:utf8 -*-

class BinaryTree:
    def __init__(self,root):
        self.key = root
        self.left = None
        self.right = None

    # 插入左子树
    def InserLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        # 当前存在左子树，插入左子树，将当前左子树降一级
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    # 插入右子树
    def InserRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        # 当前存在右子树，插入右子树，将当前右子树降一级
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    # 访问右节点值、左节点值
    def getRightVal(self):
        return self.right

    def getLeftVal(self):
        return self.left

    # 设置根节点值，获取根节点值
    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key