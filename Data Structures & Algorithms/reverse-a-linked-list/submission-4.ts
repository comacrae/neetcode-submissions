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
     * @param {ListNode} head
     * @return {ListNode}
     */
 
    reverseList(head: ListNode | null): ListNode {
        // if head is null, return null
        if(head === null)
            return null

        // store newHead variable so we track start of the reversed list
        let newHead = head;
        // if there's a subproblem, we need to reverse that list
        if(head.next){
            // inside the subproblem, set newHead as the reversed list
            newHead = this.reverseList(head.next);
            //set current head.next.next to point to head (connecting reversed to unreversed part)
            head.next.next = head;
        }
            
        // set current head.next to point to null to disconnect cycle
        head.next = null;
        // return newHead (now the head of the reversed part)
        return newHead;
    }
}
