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
    public ListNode DeleteDuplicates(ListNode head) {
        ListNode l1 = head;
        while(l1!=null)
        {
            while(l1.next!=null && l1.next.val==l1.val)
            {
                l1.next=l1.next.next;
            }
            l1=l1.next;
        }
        return head;
    }
}


#old account code
/* public class Solution {
    public ListNode DeleteDuplicates(ListNode head) {
        if(head==null) return null;
        ListNode node=head;
        while(node.next!=null)
        {
            if(node.next.val == node.val)
            {
               
                node.next=node.next.next;
            }
            else{
            if(node.next!=null)
                node=node.next;
            }
        }
        return head;
    }
} */