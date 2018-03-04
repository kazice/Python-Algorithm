class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(c**.5) + 1):
            print a
            print any((((c-a**2)**.5)%1 == 0))

m = Solution()
m.judgeSquareSum(5)