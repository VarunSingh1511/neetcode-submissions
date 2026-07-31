# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        mid = slow

        while slow:
            tmp = slow
            slow = slow.next 
            tmp.next = prev
            prev = tmp

        slow2 = head
        fast = prev

        while fast != mid:
            tmp = slow2
            slow2 = slow2.next
            tmp.next = fast

            tmp = fast
            fast = fast.next
            tmp.next = slow2
            


