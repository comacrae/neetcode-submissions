/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode {
        // set up dummy and output ptr
        const dummy = new ListNode();
        let curr = dummy;
        // while both lists have nodes left:
        while(list1 !== null && list2 !== null){
            // if a <= b, set curr.next = a and a = a.next
            if(list1.val <= list2.val){
                curr.next = list1;
                list1 = list1.next;
            }else{
                //else set curr.next = b and b = b.next
                curr.next = list2;
                list2 = list2.next
            }
            curr = curr.next;
        }
        if(list1){
            curr.next = list1;
        }else if (list2){
            curr.next = list2;
        }
        // set curr to the left overs
        //return head 
        return dummy.next;
    }
}
