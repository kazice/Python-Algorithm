#!/usr/bin/python
# -*- coding:utf8 -*-


"""
这里有一个公式，可以解决所有这类的问题，它分为四步走：
1. 判定条件为start+1小于end，start=0, end=size-1
2. mid=start+((end-start)>>1)
3. 如果data[mid]满足条件直接返回，如果满足条件的数据在mid的右边则将start=mid，如果满足条件的数据在mid左边则将end=mid
4. 根据条件再次判定start，end两个元素是否满足条件
其实整个过程就不断缩小范围的过程，最后一步就是将整个数组的范围缩小到start end两个元素而已。
"""
def guess(num):
    if num > des:
        return -1
    elif num < des:
        return 1
    else:
        return 0



def Twodivide(num):
    start, end = 0, num
    while start < end:
        mid = (start + end)/2
        if guess(mid) == 1:
            start = mid + 1
        else:
            end = mid
    return start