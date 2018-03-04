#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/3 22:59
# @Author  : Aries
# @Site    : 
# @File    : uniqueString.py
# @Software: PyCharm

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    import re
    r = '[ ’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
    pos = re.sub(r, '', s).lower()
    print(pos)
    neg = pos[::-1]
    print(neg)
    return pos == neg
isPalindrome('a ba')
