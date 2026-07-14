# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr : ListNode = head
        nxt : Optional[ListNode] = curr.next
        while nxt:
            tmp : ListNode = ListNode(nxt.val, nxt.next)
            nxt.next = curr
            if curr.next == nxt:
                curr.next = None
            curr = nxt
            nxt = tmp.next
        return curr
             