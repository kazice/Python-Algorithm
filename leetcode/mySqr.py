class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            print 0
            return 0
        else:
            i = 0.5 * x
            while (True):
                j = (i + x / i) / 2.0
                if (abs(i - j) < 0.000000000005):
                    break
                i = j
            print int(j)
            return int(j)

m = Solution()
print m.mySqrt(0)