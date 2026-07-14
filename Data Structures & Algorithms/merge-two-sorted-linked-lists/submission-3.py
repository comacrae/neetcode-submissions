# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list : Optional[ListNode] = ListNode(0, None)
        curr = merged_list
        ptr_a = list1
        ptr_b = list2

        
        while ptr_a and ptr_b:
            if ptr_a.val < ptr_b.val:
                curr.next = ListNode(ptr_a.val, None)
                ptr_a = ptr_a.next
            else:
                curr.next = ListNode(ptr_b.val, None)
                ptr_b = ptr_b.next
            curr = curr.next
        if ptr_a:
            curr.next = ListNode(ptr_a.val, ptr_a.next)
        if ptr_b:
            curr.next = ListNode(ptr_b.val, ptr_b.next)
        return merged_list.next
            

        '''
        1 , 2 , 4

        1 , 3 , 5

        1
        ''' 
