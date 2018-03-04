#!/usr/bin/python
# -*- coding:utf8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        tree = root
        num = pre_order(tree)
        result = twoSum(num, k)
        return result

    def pre_order(tree):
        num = []
        if tree == None:
            return
        num.append(tree.val)
        pre_order(tree.left)
        pre_order(tree.right)

        result = tuple(num)
        return num

    def twoSum(num, k):
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
                        sort.append(i + 1)
                    elif num[i] == nums[right]:
                        sort.append(i + 1)
                    if len(sort) == 2:
                        break
                break
            elif k < sums:
                right -= 1
            else:
                left += 1
        result = bool(sort)
        return result
