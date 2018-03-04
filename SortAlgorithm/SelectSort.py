#!/usr/bin/python
# -*- coding:utf8 -*-

# 选择排序
"""
初始时在序列中找到最小（大）元素，放到序列的起始位置作为已排序序列；
然后，再从剩余未排序元素中继续寻找最小（大）元素，放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
"""
"""
冒泡排序通过依次交换相邻两个顺序不合法的元素位置，
从而将当前最小（大）元素放到合适的位置；
而选择排序每遍历一次都记住了当前最小（大）元素的位置，
最后仅需一次交换操作即可将其放到合适的位置。
"""

def SelectSort(num):
    print num
    return num

SelectSort([6, 5, 3, 1, 8, 7, 2, 4 ])