#!/usr/bin/python
# -*- coding:utf8 -*-

# 插入排序
"""
具体算法描述如下：
1、从第一个元素开始，该元素可以认为已经被排序
2、取出下一个元素，在已经排序的元素序列中从后向前扫描
3、如果该元素（已排序）大于新元素，将该元素移到下一位置
4、重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5、将新元素插入到该位置后
6、重复步骤2~5
"""

def insertSort(num):
    length = len(num)
    i = 1
    while i < length:
        get = num[i]
        j = i - 1
        while j >= 0 and num[j] > get:
            num[j+1] = num[j]
            j -= 1
        num[j+1] = get
        i += 1

    print num
    return num

insertSort([6, 5, 3, 1, 8, 7, 2, 4 ])