#!/usr/bin/python
# -*- coding:utf8 -*-

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # 检测一个数字是否是回文，如果是则输出True,否输出False
    m = x
    result = 0
    if x >= 0:
        while x > 0:
            lastDigit = x - x / 10 * 10
            result = result * 10 + lastDigit
            x /= 10
        if result == m:
            result = True
        else:
            result = False
    else:
        result = False
    print(result)
    return result


isPalindrome(-33333)
