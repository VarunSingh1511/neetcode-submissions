# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        tsum = ListNode(0)
        cur = tsum
        carryOver = 0

        while l1 and l2:
            sumdig = l1.val + l2.val + carryOver
            print(sumdig)
            if sumdig > 9:
                carryOver = 1
                sumdig = sumdig%10
                
            else:
                carryOver = 0

            newNode = ListNode(sumdig)
            cur.next = newNode
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sumdig = l1.val + carryOver
            if sumdig > 9:
                carryOver = 1
                sumdig = sumdig%10
                
            else:
                carryOver = 0

            newNode = ListNode(sumdig)
            cur.next = newNode
            cur = cur.next
            l1 = l1.next

        while l2:
            sumdig = l2.val + carryOver
            if sumdig > 9:
                carryOver = 1
                sumdig = sumdig%10
                
            else:
                carryOver = 0

            newNode = ListNode(sumdig)
            cur.next = newNode
            cur = cur.next
            l2 = l2.next

        if carryOver == 1:
            cur.next = ListNode(1)

        tsum = tsum.next

        return tsum
                
