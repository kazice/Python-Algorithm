#!/usr/bin/python
# -*- coding:utf8 -*-

# 冒泡排序
"""
冒泡排序算法的运作如下：
1、比较相邻的元素，如果前一个比后一个大，就把它们两个调换位置。
2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3、针对所有的元素重复以上的步骤，除了最后一个。
4、持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""
def BubbleSort(num):
    length = len(num)
    j = 0
    while j < length - 1:
        i = 0
        while i < length - j - 1:
            if num[i] > num[i+1]:
                num[i],num[i+1] = num[i+1],num[i]
            i += 1
        j += 1

    print(num)
    return num

BubbleSort([6, 5, 3, 1, 8, 7, 2, 4 ])

# python中没有for (int j = 0; j < n - 1; j++)的语法
# 一顿摸索之后，我领悟到了用while代替上述语法，具体结构如下：
# i = 初值
# while 循环控制条件：
#   循环执行语句
#   i = xxx(i保证能退出循环的条件)
# 如果是嵌套循环的话，就像我这个冒泡排序算法一样写，注意j、i赋初值的位置