class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        cur1 = list1
        cur2 = list2
        if cur1.val <= cur2.val:
            head = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur2 = cur2.next

        temp = head
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                temp.next = cur1
                cur1 = cur1.next
            else:
                temp.next = cur2
                cur2 = cur2.next
            temp = temp.next

        while cur1:
            temp.next = cur1
            cur1 = cur1.next
            temp = temp.next
        
        while cur2:
            temp.next = cur2
            cur2 = cur2.next
            temp = temp.next

        return head