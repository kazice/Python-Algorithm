#!/usr/bin/python
# -*- coding:utf8 -*-

def twoSum(num,target):
    # 输入一个由数字元素组成的列表和一个目标值，要求确定列表中的两数相加是否等于目标值
    nums = sorted(num)
    left = 0
    length = len(nums)
    right = length - 1
    sort = []
    while left < right:
        sums = nums[left] + nums[right]

        if target == sums:
            for i in range(length):
                if num[i] == nums[left]:
                    sort.append(i+1)
                elif num[i] == nums[right]:
                    sort.append(i+1)
                if len(sort) == 2:
                    break
            break
        elif target < sums:
            right -= 1
        else:
            left += 1
    result = tuple(sort)
    print result
    return result


# 函数使用示例
twoSum([2,34,3,9,1],3)
