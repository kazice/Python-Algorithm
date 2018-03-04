class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        if digits.count(9) == len(digits):
            digits[:] = [0] * len(digits)
            digits.insert(0, 1)
        else:
            if digits[i] != 9:
                digits[i] += 1
            elif digits.count(9) == len(digits) - 1 and digits[0] != 9:
                digits[1:] = [0]*(len(digits)-1)
                digits[0] += 1
            else:
                while i > -len(digits):
                    if digits[i] == 9:
                        digits[i] = 0
                        i -= 1
                    else:
                        digits[i] += 1
                        break
        print digits
        return digits

m = Solution()
m.plusOne([2,4,9,3,9])