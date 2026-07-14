/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
 
public class Solution {
    public ListNode GetLast(ListNode head){
        if(head == null){
            return null;
        }else if (head.next == null){
            return head;
        }else{ // if 2 or more nodes in list
            ListNode newHead = null;
            ListNode curr = head;
            while(curr.next.next != null){
                curr = curr.next;
            }
            // now second to last
            newHead = curr.next;
            curr.next = null;
            newHead.next = GetLast(head);
            return newHead;
        }
    }
    public ListNode ReverseList(ListNode head) {
        return GetLast(head);
    }
}
