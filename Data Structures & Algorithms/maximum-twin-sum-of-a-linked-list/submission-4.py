# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast = head,head
        maxsum = 0
        prev = None

        while fast:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        while slow:
            maxsum = max(maxsum, slow.val + prev.val)
            prev = prev.next
            slow = slow.next

        return maxsum      
            