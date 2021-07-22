public class Solution {
    ListNode l3;
    ListNode firstl3;
    public ListNode MergeTwoLists(ListNode l1, ListNode l2) {
        
        while(l1!=null || l2!=null){
            if(l1!=null && l2!=null){
                if(l1?.val<l2?.val) {addtol3(l1.val);l1=l1.next;}
                else {addtol3(l2.val);l2=l2.next;}
            }
            else if(l1==null) {addtol3(l2.val);l2=l2.next;}
            else {addtol3(l1.val);l1=l1.next;}
        }
        return firstl3;
    }
    public void addtol3(int val)
    {
        if(l3!=null){
        l3.next = new ListNode(val); 
        l3= l3.next;}
        else {l3= new ListNode(val);firstl3=l3;}
       
    }
}