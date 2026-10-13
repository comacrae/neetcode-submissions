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
        const hashset: Set<ListNode> = new Set<ListNode>();
        while(head != null){
            if (hashset.has(head)) return true;
            else{
                hashset.add(head);
                head=head.next;
            }
        }
        return false;
    }
}
