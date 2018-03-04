class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums
        nums[:] = set(nums)
        print num
        print nums
        print 2*sum(nums)-sum(num)
        return 2*sum(nums)-sum(num)


m = Solution()
m.singleNumber([1,2,2])