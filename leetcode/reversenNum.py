#!/usr/bin/python
# -*- coding:utf8 -*-

def reverse(num):
    # 数字翻转，输入一个32位的整数，输出他的翻转数字
    if num > 0:
        flag = 1
    else:
        flag = 0
        num = -num
    result = 0
    while num > 0:
        lastDigit = num - num/10 * 10
        result = result*10 + lastDigit
        num /= 10
    if result > 2147483648:
        result = 0
    else:
        if flag == 0:
            result = -result
    print result
    return result

# 函数使用示例
reverse(1)