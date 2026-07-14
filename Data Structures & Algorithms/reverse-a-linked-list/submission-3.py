# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a: Optional[ListNode] = head
        if not a: 
            return None
        b: Optional[ListNode] = a.next
        if not b:
            return a
        while b.next:
            b = b.next
            a = a.next
        a.next = None
        b.next = self.reverseList(head)
        return b
