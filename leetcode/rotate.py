#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/3 22:32
# @Author  : Aries
# @Site    : 
# @File    : rotate.py
# @Software: PyCharm


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nums = nums[len(nums) - k:len(nums)] + nums[0:len(nums) - k]
    print(nums)

rotate([1,2,3,4,5,6,7],3)