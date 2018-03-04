#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 0:27
# @Author  : Aries
# @Site    : 
# @File    : twoListSort.py
# @Software: PyCharm


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    i, j = m, n
    nums1[:] = nums1 + [0]*n
    print(nums1)
    while i > 0:
        while j > 0:
            if nums1[i - 1] >= nums2[j - 1]:
                nums1[i + j - 1] = nums1[i - 1]
                i -= 1
            else:
                nums1[i + j - 1] = nums2[j - 1]
                j -= 1
            print(nums1)
    print(nums1)

merge([0],0,[1],1)

