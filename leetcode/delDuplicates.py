# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fir, sec = head,head.next if head else None
        while sec:
            if fir.val == sec.val:
                sec = sec.next
                fir.next = sec
            else:
                fir = sec
                sec = sec.next
        return head

m = Solution()
m.deleteDuplicates([1, 2, 2])
