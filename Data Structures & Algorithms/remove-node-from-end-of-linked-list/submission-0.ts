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
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head: ListNode | null, n: number): ListNode {
        // init prev and curr pointers
        let prev = null;
        let curr = head;
        let size = 0;
        // get size of list
        while(curr){
            curr = curr.next;
            size += 1;
        }
        // if size == n, return head.next
        if(size == n)
            return head.next;
        // else init prev = null, curr =  head
        prev = null;
        curr = head;

        for(let i = 0; i < (size - n); i++){
            // for i = 0 to i < (size - n)
            // move curr forward and prev forward
            prev = curr;
            curr = curr.next;
        }
        prev.next = curr.next;
        // point prev.next to curr.next
        // return head
        return head;

    }
}
