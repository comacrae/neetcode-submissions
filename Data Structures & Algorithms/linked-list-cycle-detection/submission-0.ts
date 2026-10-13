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
        let a : ListNode | null = head;
        let b = a;
        let counter:number = 0;

        while(b != null && counter < 1000)
        {
            b = b.next;
            counter += 1;
        }
        while(a != b) a = a.next;
        
        return a !== null;
    }
}
