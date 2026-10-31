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
        //iterative solution

        //start prev at dummy head
        let prev = null;
        // start curr at head
        let curr = head

        // while curr exists
        while(curr){
            // set temp to curr.next
            let tmp = curr.next;
            // set curr.next to prev
            curr.next = prev;
            // set prev to curr
            prev = curr;
            // set curr to tmp
            curr = tmp;
        }
        return prev;
        // return prev bc its the new head
    }
}
