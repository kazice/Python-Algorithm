#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/3 13:06
# @Author  : Aries
# @Site    : 
# @File    : triangle.py
# @Software: PyCharm


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 2:
            return [[1]*numRows]
        num = [[1], [1, 1]]
        for i in range(2, numRows):
            num.append([])
            num[i].append(1)
            j = 1
            while j < i:
                num[i].append(num[i-1][j-1] + num[i-1][j])

                j += 1
            num[i].append(1)
        print(num)
        return num

m = Solution()
m.generate(6)