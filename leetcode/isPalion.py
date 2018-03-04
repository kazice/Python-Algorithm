#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/4 1:28
# @Author  : Aries
# @Site    : 
# @File    : isPalion.py
# @Software: PyCharm

# def validPalindrome(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     if s[::-1] == s:
#         return True
#     else:
#         for k in range(len(s)):
#             print((s[0:k] + s[k + 1:len(s)]))
# validPalindrome('deeee')


class Solution(object):
    def isVersion(self, n):
        if n == 1:
            return True
        else:
            return False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.isVersion(n):
            print(n)
            return n
        else:
            print(n)
            n -= 1
            self.firstBadVersion(n)

m = Solution()
m.firstBadVersion(2)