# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev = ListNode()
        n1, n2 = head, head.next
        head = prev

        while n1 is not None and n2 is not None:
            prev.next = n2
            n1.next = n2.next
            n2.next = n1
            prev = n1
            n1 = n1.next
            if n1 is None:
                return head.next
            n2 = n1.next
        
        return head.next


        