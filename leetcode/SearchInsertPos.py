#!/usr/bin/python
# -*- coding:utf8 -*-

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    m = 0
    i = 0
    while i < (len(nums)):
        if nums[i] >= target:
            m = i
            break
        else:
            i += 1
    if target > nums[len(nums)-1]:
        m = len(nums)
    print(m)
    return m

searchInsert([1,3],3)