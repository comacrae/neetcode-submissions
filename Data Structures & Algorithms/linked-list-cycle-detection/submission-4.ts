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
     * @return {boolean}
     */
    hasCycle(head: ListNode | null): boolean {
        let a = head;
        let b = a;
        while(b != null && a != null){
            b = b.next;
            if(b === null) return false;
            b = b.next;
            if (b === a) return true;
            a = a.next;
        }
        return false;
    }
}
