#!/usr/bin/python
# -*- coding:utf8 -*-

# 定向冒泡排序，又叫鸡尾酒排序
# 此算法与冒泡排序的不同处在于从低到高然后从高到低

def orientBubbleSort(num):
    length = len(num)
    left, right = 0, length-1
    while left < right:
        i = left
        while i < right:
            if num[i] > num[i+1]:
                num[i],num[i+1] = num[i+1],num[i]
            i += 1
        right -= 1
        j = right
        while j > left:
            if num[j-1] > num[j]:
                num[j-1],num[j] = num[j],num[j-1]
            j -= 1
        left += 1
    print num
    return num

orientBubbleSort([6, 5, 3, 1, 8, 7, 2, 4 ])