"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps.
 You need to find minimum cost to reach the top of the floor,
 and you can either start from the step with index 0, or the step with index 1.
"""

"""
解题思路：
假设已到达第i步，则他是由前i-1步或者是前i-2步构成的，加上对应的cost[i]值
一直递推到最后
"""
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        fir = cost[0]
        sec = cost[1]
        for i in range(2,len(cost)):
            fir,sec = sec,min(fir,sec) + cost[i]
        return min(fir,sec)

m = Solution()
m.minCostClimbingStairs([1,3,4,5,2,35,6])
