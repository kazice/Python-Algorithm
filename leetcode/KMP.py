class Solution:
    def KMP(self,s,p):
        return True



    def getNext(self,p):
        next = [-1]
        k,j = -1,0
        pLen = len(p)
        while j < pLen:
            if k == -1 or p[j] == p[k]:
                k += 1
                j += 1
                next.append(k)
            else:
                k = next[k]
        NEXT = next[:-1]
        print NEXT

m = Solution()
m.getNext('ABCDABD')
