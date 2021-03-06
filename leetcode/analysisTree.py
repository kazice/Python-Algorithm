#!/usr/bin/python
# -*- coding:utf8 -*-

# 使用 (3+(4*5))这个表达式构造解析树
# 表达式分解为如下的字符列表：['(', '3', '+', '(', '4', '*', '5' ,')',')']

"""
 如果当前读入的字符是'('，添加一个新的节点作为当前节点的左子节点，并下降到左子节点处。
 如果当前读入的字符在列表['+', '-', '/', '*']中，将当前节点的根值设置为当前读入的字符。添加一个新的节点作为当前节点的右子节点，并下降到右子节点处。
 如果当前读入的字符是一个数字，将当前节点的根值设置为该数字，并返回到它的父节点。
 如果当前读入的字符是’)’，返回当前节点的父节点。
"""

# 通过上述的规则，使用栈和二叉树来操作