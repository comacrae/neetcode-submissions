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
     * @return {void}
     */

    reverseList(head:ListNode | null): ListNode | null{
        if(head === null)
            return head;
        let curr = head;
        let prev = null;
        while(curr){
            let next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    getSecondSplit(head:ListNode | null): ListNode | null{
        //split lists halfway and return pointer to second half
        if(head === null)
            return head;
        let totalNodes: number = 1;
        let curr = head;
        while(curr){
            curr = curr.next;
            totalNodes +=1
        }
        const halfwayIdx = Math.floor(totalNodes / 2);
        let halfwayStart = head;
        for(let i = 0; i < halfwayIdx-1; i++){
            halfwayStart = halfwayStart.next;
        }
        //track one before the split so we can clip
        let end = halfwayStart;
        halfwayStart = halfwayStart.next;
        end.next = null; // split the lists
        return halfwayStart;
    }
    mergeLists(a:ListNode|null, b:ListNode|null){
        let aNext = null;
        let bNext = null;
        while(a !== null && b !== null){
            aNext = a.next;
            bNext = b.next;
            a.next = b;
            if(aNext !== null)
                b.next = aNext
            a = aNext;
            b = bNext;
        }
    }
    reorderList(head: ListNode | null): void {
        //split
        let secondHalf = this.getSecondSplit(head);
        //reverse second half
        secondHalf = this.reverseList(secondHalf);
        //merge two halves
        this.mergeLists(head, secondHalf);
        
    }
}
